from django import forms
from django.contrib.contenttypes.models import ContentType
from thecut.media import MEDIA_SOURCE_CLASSES
from thecut.media.models import AttachedMediaItem


class AttachedMediaItemInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttachedMediaItemInlineForm, self).__init__(*args,
            **kwargs)
        
        content_types = []
        for model in MEDIA_SOURCE_CLASSES:
            content_types += [ContentType.objects.get_for_model(model)]
        
        queryset = self.fields['content_type'].queryset
        self.fields['content_type'].queryset = queryset.filter(
            pk__in=[ct.pk for ct in content_types])
        
    class Media:
        css = {'all': ['media/admin.css']}
        js = ['media/jquery.js', 'media/jquery-ui.js',
            'media/jquery.init.js', 'media/csrf.js', 'media/admin.js']
    
    class Meta:
        model = AttachedMediaItem

