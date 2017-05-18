# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .. import settings
from ..forms import MediaUploadForm
from ..utils import get_metadata
from django.contrib.admin.options import csrf_protect_m
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.utils.encoding import force_text, force_unicode
from django.utils.safestring import mark_safe
from django.views import generic

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class AdminAddMixin(object):

    template_name = 'change_form.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super(AdminAddMixin, self).get_context_data(*args,
                                                                   **kwargs)

        admin = self.kwargs['admin']
        form = context_data.get('form', kwargs.get('form'))
        opts = admin.model._meta
        content_type = ContentType.objects.get_for_model(admin.model)

        defaults = {'current_app': admin.admin_site.name, 'opts': opts,
                    'app_label': opts.app_label, 'add': True,
                    'content_type': content_type, 'form_url': '',
                    'title': 'Add {0}'.format(
                        force_unicode(opts.verbose_name)),
                    'root_path': getattr(admin.admin_site, 'root_path', None),
                    'media': mark_safe(admin.media + form.media),
                    'errors': form.errors,

                    'change': False, 'is_popup': False, 'save_as': False,
                    'save_on_top': False, 'show_delete': False,
                    'has_file_field': True,
                    'has_add_permission': self.has_add_permission(),
                    'has_change_permission': self.has_change_permission(),
                    'has_delete_permission': self.has_delete_permission(),
                    'content_type_id': content_type.id,
                    'change_form_template': '{0}/change_form.html'.format(
                        admin.admin_site.name),
                    }

        for key, value in defaults.items():
            context_data.setdefault(key, value)

        return context_data

    def get_success_url(self, *args, **kwargs):
        admin_site = self.kwargs['admin'].admin_site.name
        app_label = self.kwargs['admin'].model._meta.app_label
        model_name = self.kwargs['admin'].model._meta.object_name.lower()
        msg_dict = {
            'name': force_text(self.kwargs['admin'].model._meta.verbose_name),
            'object': force_text(self.object)}
        reverse_args = []

        if '_addanother' in self.request.POST:
            message = ('The {name} "{object}" was added successfully. You '
                       'may add another {name} below.'.format(**msg_dict))
            url = '{admin_site}:{app_label}_{model_name}_add'
        elif '_continue' in self.request.POST:
            message = ('The {name} "{object}" was added successfully. You '
                       'may edit it again below.'.format(**msg_dict))
            reverse_args += [self.object.pk]
            url = '{admin_site}:{app_label}_{model_name}_change'
        else:
            message = 'The {name} "{object}" was added successfully.'.format(
                **msg_dict)
            url = '{admin_site}:{app_label}_{model_name}_changelist'

        messages.add_message(self.request, messages.SUCCESS, message)
        return reverse(url.format(admin_site=admin_site, app_label=app_label,
                                  model_name=model_name), args=reverse_args)

    def get_template_names(self):
        admin = self.kwargs['admin']
        current_app = admin.admin_site.name
        app_label = admin.model._meta.app_label
        model_name = admin.model._meta.object_name.lower()

        return [
            '{admin}/{app}/{model}/{template}'.format(
                admin=current_app, app=app_label, model=model_name,
                template=self.template_name),
            '{admin}/{app}/{template}'.format(admin=current_app, app=app_label,
                                              template=self.template_name),
            '{admin}/{template}'.format(admin=current_app,
                                        template=self.template_name),
            'admin/{app}/{model}/{template}'.format(
                app=app_label, model=model_name, template=self.template_name),
            'admin/{app}/{template}'.format(app=app_label,
                                            template=self.template_name),
            'admin/{template}'.format(template=self.template_name)]

    @csrf_protect_m
    def dispatch(self, request, *args, **kwargs):
        if not kwargs['admin'].has_add_permission(request):
            raise PermissionDenied()
        return super(AdminAddMixin, self).dispatch(request, *args, **kwargs)

    def has_add_permission(self):
        return self.kwargs['admin'].has_add_permission(self.request)

    def has_change_permission(self):
        return self.kwargs['admin'].has_change_permission(self.request)

    def has_delete_permission(self):
        return self.kwargs['admin'].has_delete_permission(self.request)


class UploadView(AdminAddMixin, generic.FormView):

    form_class = MediaUploadForm

    template_name = 'media_upload_form.html'

    def form_valid(self, form):
        admin = self.kwargs['admin']
        model = admin.model
        files = form.files.getlist('files')

        for upload in files:
            obj = model(title=form.cleaned_data['title'], file=upload,
                        created_by=self.request.user,
                        updated_by=self.request.user)

            if settings.USE_EXIFTOOL:
                # Try to populate missing data from the file's metadata
                metadata = get_metadata(upload)
                obj.title = obj.title or metadata.get('XMP:Title', '')[:200]
                obj.caption = obj.caption or metadata.get('XMP:Description',
                                                          '')

            obj.save()
            tags = self.get_tags(form, upload)
            obj.tags.add(*tags)

            self.object = obj  # Set last object procesed on view

        return super(UploadView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context_data = super(UploadView, self).get_context_data(*args,
                                                                **kwargs)
        plural_name = force_unicode(
            self.kwargs['admin'].model._meta.verbose_name_plural)
        context_data.update({'title': 'Add {0}'.format(plural_name)})
        return context_data

    def get_tags(self, form, upload):
        tags = []
        if settings.USE_EXIFTOOL:
            metadata = get_metadata(upload)
            keywords = metadata.get('IPTC:Keywords')
            tags = keywords if isinstance(keywords, list) else [keywords]

        return form.cleaned_data['tags'] or tags

    def get_content_types(self):
        admin = self.kwargs['admin']
        return getattr(admin.model, 'content_types', None)

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(UploadView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs.update(content_types=self.get_content_types())
        return form_kwargs
