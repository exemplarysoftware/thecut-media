# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import AdminAddMixin
from s3upload.views import DropzoneS3UploadFormView


class DropzoneUploadView(AdminAddMixin, DropzoneS3UploadFormView):
    # Assumes FileField with name of 'file' on model.

    template_name = 'dropzone_form.html'

    def _get_field(self):
        return self._get_model()._meta.get_field_by_name('file')[0]

    def _get_model(self):
        return self.kwargs['admin'].model

    def form_valid(self, form, *args, **kwargs):
        self._get_model().objects.create(file=form.get_file_path(),
                                         created_by=self.request.user,
                                         updated_by=self.request.user)
        return super(DropzoneUploadView, self).form_valid(form)

    def get_storage(self):
        return self._get_field().storage

    def get_upload_to(self):
        return self._get_field().generate_filename(
            self._get_model(), '').rstrip('.')
