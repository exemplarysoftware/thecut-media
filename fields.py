from django.forms import ModelMultipleChoiceField, MultipleChoiceField
from django.forms.util import ValidationError
from django.utils.encoding import force_unicode
from media.widgets import DocumentSelectMultiple, GallerySelectMultiple, ImageSelectMultiple


class DocumentMultipleChoiceField(ModelMultipleChoiceField):
    """ModelMultipleChoiceField with ajax document picker."""
    widget = DocumentSelectMultiple()


class GalleryMultipleChoiceField(ModelMultipleChoiceField):
    """ModelMultipleChoiceField with ajax gallery picker."""
    widget = GallerySelectMultiple()


class ImageMultipleChoiceField(MultipleChoiceField):
    """MultipleChoiceField with ajax image picker, and drag-and-drop ordering."""
    widget = ImageSelectMultiple()

