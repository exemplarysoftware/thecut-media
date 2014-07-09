# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from distutils.version import StrictVersion
from django import get_version
from django.contrib.admin.options import csrf_protect_m
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from thecut.media.mediasources import settings
from thecut.media.mediasources.forms import MediaUploadForm
from thecut.media.mediasources.utils import get_metadata

if StrictVersion(get_version()) < StrictVersion('1.3'):
    # Pre-Django 1.3 compatibility
    import cbv as generic
else:
    from django.views import generic


class UploadView(generic.FormView):
    form_class = MediaUploadForm
    success_url = '../'

    @csrf_protect_m
    def dispatch(self, request, *args, **kwargs):
        if not kwargs['admin'].has_add_permission(request):
            raise PermissionDenied()
        return super(UploadView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        admin = self.kwargs['admin']
        model = admin.model
        files = form.files.getlist('files')

        for upload in files:
            obj = model(title=form.cleaned_data['title'], file=upload,
                        tags=form.cleaned_data['tags'],
                        created_by=self.request.user,
                        updated_by=self.request.user)

            if settings.USE_EXIFTOOL:
                # Try to populate missing data from the file's metadata
                metadata = get_metadata(upload)
                obj.title = obj.title or metadata.get('XMP:Title', '')[:200]
                obj.caption = obj.caption or metadata.get('XMP:Description',
                                                          '')
                tags = ['{0}'.format(keyword) for keyword in metadata.get(
                        'IPTC:Keywords', [])]
                if not obj.tags:
                    obj.tags = ' '.join('"{0}"'.format(tag) if ' ' in tag else
                                        tag for tag in tags)

            obj.save()

        return super(UploadView, self).form_valid(form)

    def get_content_types(self):
        admin = self.kwargs['admin']
        return getattr(admin.model, 'content_types', None)

    def get_context_data(self, *args, **kwargs):
        context_data = super(UploadView, self).get_context_data(*args,
                                                                **kwargs)

        admin = self.kwargs['admin']
        form = kwargs['form']
        opts = admin.model._meta
        content_type = ContentType.objects.get_for_model(admin.model)

        defaults = {'current_app': admin.admin_site.name, 'opts': opts,
                    'app_label': opts.app_label, 'add': True,
                    'content_type': content_type, 'form_url': '',
                    'title': 'Add {0}'.format(
                        force_unicode(opts.verbose_name_plural)),
                    'root_path': getattr(admin.admin_site, 'root_path', None),
                    'media': mark_safe(admin.media + form.media),
                    'errors': form.errors,

                    'change': False, 'is_popup': False, 'save_as': False,
                    'save_on_top': False, 'show_delete': False,
                    'has_file_field': True, 'has_add_permission': False,
                    'has_change_permission': False,
                    'has_delete_permission': False,
                    'content_type_id': content_type.id,
                    'change_form_template': '{0}/change_form.html'.format(
                        admin.admin_site.name),
                    }

        for key, value in defaults.items():
            context_data.setdefault(key, value)
        return context_data

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(UploadView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs.update(content_types=self.get_content_types())
        return form_kwargs

    def get_template_names(self):
        admin = self.kwargs['admin']
        current_app = admin.admin_site.name
        app_label = admin.model._meta.app_label
        model_name = admin.model._meta.object_name.lower()

        return [
            '{0}/{1}/{2}/media_upload_form.html'.format(current_app, app_label,
                                                        model_name),
            '{0}/{1}/media_upload_form.html'.format(current_app, app_label),
            '{0}/media_upload_form.html'.format(current_app),
            'admin/{0}/{1}/media_upload_form.html'.format(app_label,
                                                          model_name),
            'admin/{0}/media_upload_form.html'.format(app_label),
            'admin/media_upload_form.html']

    def render_to_response(self, *args, **kwargs):
        admin = self.kwargs['admin']
        current_app = admin.admin_site.name
        return super(UploadView, self).render_to_response(
            *args, current_app=current_app, **kwargs)
