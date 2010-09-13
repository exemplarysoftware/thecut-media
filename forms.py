from django.forms import CharField, HiddenInput, ModelForm
from media.fields import DocumentMultipleChoiceField, GalleryMultipleChoiceField, ImageMultipleChoiceField
from media.models import Document, MediaSet
from photologue.models import Photo, Gallery


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
    
 #   def save(self, *args, **kwargs):
 #       mediaset = super(MediaSetForm, self).save(*args, **kwargs)
 #       image_pks = self.cleaned_data['images']
 #       image_order = ','.join(image_pks)
 #       mediaset.image_order = image_order
 #       if kwargs.get('commit', False):# and mediaset.pk:
 #           mediaset.save()
 #           print '----- saved order: %s' %(mediaset.image_order)
 #       else:
 #           print '----- unsaved order: %s' %(mediaset.image_order)
 #       return mediaset

