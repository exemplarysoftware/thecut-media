# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from s3upload.views import DropzoneS3UploadFormView

from . import AdminAddMixin
from ..forms.s3upload import ContentTypeValidateS3UploadForm


class DropzoneUploadView(AdminAddMixin, DropzoneS3UploadFormView):
    # Assumes FileField with name of 'file' on model.

    template_name = 'dropzone_form.html'

    validate_upload_form_class = ContentTypeValidateS3UploadForm

    def _get_field(self):
        return self._get_model()._meta.get_field('file')

    def _get_model(self):
        return self.kwargs['admin'].model

    def form_valid(self, form, *args, **kwargs):
        response = super(DropzoneUploadView, self).form_valid(form)
        self._get_model().objects.create(file=form.get_processed_path(),
                                         created_by=self.request.user,
                                         updated_by=self.request.user)
        return response

    def get_storage(self):
        return self._get_field().storage

    def get_process_to(self):
        return self._get_field().generate_filename(
            self._get_model(), '').rstrip('.')

    def get_processed_key_generator(self):

        def generate_key(process_to, upload_name):
            path = os.path.join(process_to, upload_name)
            return self.get_storage().get_available_name(path)

        return generate_key

    def get_validate_upload_form_kwargs(self, *args, **kwargs):
        kwargs = super(DropzoneUploadView,
                       self).get_validate_upload_form_kwargs(*args, **kwargs)
        valid_content_types = self._get_model().content_types
        kwargs.update({'valid_content_types': valid_content_types})
        return kwargs
