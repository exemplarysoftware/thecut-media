from django.forms import CharField, HiddenInput, ModelForm
from media.fields import DocumentMultipleChoiceField, GalleryMultipleChoiceField, ImageMultipleChoiceField
from media.models import Document, MediaSet
from photologue.models import Photo, Gallery


class MediaSetForm(ModelForm):
    images = ImageMultipleChoiceField(
        choices=[(p.pk, p.title) for p in Photo.objects.all()],
        required=False)
    galleries = GalleryMultipleChoiceField(Gallery.objects.all(),
        required=False)
    documents = DocumentMultipleChoiceField(Document.objects.all(),
        required=False)
    
    class Meta:
        fields = ['images', 'galleries', 'documents']
        model = MediaSet
    
    def __init__(self, *args, **kwargs):
        super(MediaSetForm, self).__init__(*args, **kwargs)
        if self.instance:
            # Set initial selections for choices, and reorder choice
            # options to reflect attached photo ordering.
            self.initial['images'] = [ap.photo.pk for ap in \
                self.instance.attachedphoto_set.all()]
            choices = self.fields['images'].choices
            for image_pk in self.initial['images']:
                image = Photo.objects.get(pk=image_pk)
                choice = (image.pk, image.title)
                choice_index = choices.index(choice)
                choices.pop(choice_index)
                choices.append(choice)
            self.fields['images'].choices = choices
    
    def save(self, *args, **kwargs):
        mediaset = super(MediaSetForm, self).save(*args, **kwargs)
        if kwargs.get('commit', False):# and mediaset.pk:
            # Re-create attached photos with new ordering
            mediaset.photos.clear()
            image_pks = self.cleaned_data['images']
            for image_pk in image_pks:
                image = Photo.objects.get(pk=image_pk)
                order = image_pks.index(image_pk)
                mediaset.attachedphoto_set.create(
                    photo=image, order=order)
        return mediaset
    
    #def save(self, commit=True):
        # http://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields
        #instance = super(MediaSetForm, self).save(False)
        ## Prepare a 'save_m2m' method for the form,
        #old_save_m2m = self.save_m2m
        #def save_m2m():
        #   old_save_m2m()
        #   instance.photos.clear()
        #   image_pks = self.cleaned_data['images']
        #   attached_photos = []
        #   for image_pk in image_pks:
        #        image = Photo.objects.get(pk=image_pk)
        #        order = image_pks.index(image_pk)
        #        instance.attachedphoto_set.create(
        #            photo=image, order=order)
        #   instance.save()
        #self.save_m2m = save_m2m
        #
        ## Do we need to save all changes now?
        #if commit:
        #    instance.save()
        #    self.save_m2m()
        #return instance

