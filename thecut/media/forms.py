from datetime import datetime
from django.forms import CharField, HiddenInput, ModelForm
from thecut.media.fields import DocumentMultipleChoiceField, GalleryMultipleChoiceField, ImageMultipleChoiceField
from thecut.media.models import Document, Gallery, MediaSet, Video
from photologue.models import Photo


class DocumentAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentAdminForm, self).__init__(*args, **kwargs)
        self.fields['publish_at'].initial = datetime.now()
    
    class Meta:
        model = Document


class GalleryAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GalleryAdminForm, self).__init__(*args, **kwargs)
        self.fields['publish_at'].initial = datetime.now()
        image_choices = [(p.pk, p.title) for p in Photo.objects.all()]
        self.fields['images'].choices = image_choices
        
        if self.instance.image_order:
            # Reorder choice options to reflect image ordering.
            image_order = self.instance.ordered_images
            for image in image_order:
                choice = (image.pk, image.title)
                choice_index = image_choices.index(choice)
                image_choices.pop(choice_index)
                image_choices.append(choice)
            self.fields['images'].choices = image_choices
    
    images = ImageMultipleChoiceField(required=False)
    
    class Meta:
        model = Gallery


class MediaSetForm(ModelForm):
    images = ImageMultipleChoiceField(required=False)
    galleries = GalleryMultipleChoiceField(Gallery.objects.all(),
        required=False)
    documents = DocumentMultipleChoiceField(Document.objects.all(),
        required=False)
    
    class Meta:
        fields = ['images', 'image_order', 'galleries', 'documents']
        model = MediaSet
    
    def __init__(self, *args, **kwargs):
        super(MediaSetForm, self).__init__(*args, **kwargs)
        
        image_choices = [(p.pk, p.title) for p in Photo.objects.all()]
        self.fields['images'].choices = image_choices
        
        if self.instance.image_order:
            # Reorder choice options to reflect image ordering.
            image_order = self.instance.ordered_images
            for image in image_order:
                choice = (image.pk, image.title)
                choice_index = image_choices.index(choice)
                image_choices.pop(choice_index)
                image_choices.append(choice)
            self.fields['images'].choices = image_choices


class VideoAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VideoAdminForm, self).__init__(*args, **kwargs)
        self.fields['publish_at'].initial = datetime.now()
    
    class Meta:
        model = Video

