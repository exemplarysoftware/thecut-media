# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.admin.options import csrf_protect_m
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from thecut.media.mediasources.forms import MediaUploadForm

# Class-based views
from distutils.version import StrictVersion
from django import get_version
if StrictVersion(get_version()) < StrictVersion('1.3'):
    import cbv as generic
else:
    from django.views import generic


class UploadView(generic.FormView):
    form_class = MediaUploadForm
    success_url = '../'
    
    @csrf_protect_m
    def dispatch(self, request, *args, **kwargs):
        if not kwargs['admin'].has_add_permission(request):
            raise PermissionDenied
        return super(UploadView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        admin = self.kwargs['admin']
        model = admin.model
        files = self.request.FILES.getlist('files')
        
        for upload in files:
            obj = model(title=form.cleaned_data['title'], file=upload,
                tags=form.cleaned_data['tags'], created_by=self.request.user,
                updated_by=self.request.user)
            obj.save()
        
        return super(UploadView, self).form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context_data = super(UploadView, self).get_context_data(*args,
            **kwargs)
        
        admin = self.kwargs['admin']
        form = kwargs['form']
        opts = admin.model._meta
        content_type = ContentType.objects.get_for_model(admin.model)
        
        defaults = {'current_app': admin.admin_site.name,
            'opts': opts, 'app_label': opts.app_label, 'add': True,
            'content_type': content_type, 'form_url': '',
            'title': 'Add %s' %(force_unicode(opts.verbose_name_plural)),
            'root_path': admin.admin_site.root_path,
            'media': mark_safe(admin.media + form.media),
            'errors': form.errors,
            
            'change': False, 'is_popup': False, 'save_as': False,
            'save_on_top': False, 'show_delete': False, 'has_file_field': True,
            'has_add_permission': False, 'has_change_permission': False,
            'has_delete_permission': False, 'content_type_id': content_type.id,
            'change_form_template': '%s/change_form.html' %(
                admin.admin_site.name)
        }
        
        for key, value in defaults.items():
            context_data.setdefault(key, value)
        return context_data
    
    def get_template_names(self):
        admin = self.kwargs['admin']
        current_app = admin.admin_site.name
        app_label = admin.model._meta.app_label
        model_name = admin.model._meta.object_name.lower()
        
        return [
            '%s/%s/%s/media_upload_form.html' %(current_app, app_label,
                model_name),
            '%s/%s/media_upload_form.html' %(current_app, app_label),
            '%s/media_upload_form.html' %(current_app),
            'admin/%s/%s/media_upload_form.html' %(app_label, model_name),
            'admin/%s/media_upload_form.html' %(app_label),
            'admin/media_upload_form.html']

