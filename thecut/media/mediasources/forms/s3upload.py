# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from s3upload.forms import ValidateS3UploadForm


class ContentTypeValidateS3UploadForm(ValidateS3UploadForm):
    """
    Ensure the content type of an uploaded file matches one of a list of valid
    content types.

    """

    def __init__(self, *args, **kwargs):
        self.valid_content_types = kwargs.pop('valid_content_types')
        super(ContentTypeValidateS3UploadForm, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        cleaned_data = super(ContentTypeValidateS3UploadForm, self).clean(
            *args, **kwargs)
        content_type = self.get_upload_content_type()
        if content_type not in self.valid_content_types:
            raise forms.ValidationError('Content-Type not allowed.')
        return cleaned_data
