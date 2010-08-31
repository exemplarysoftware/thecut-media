from django.forms import ModelMultipleChoiceField
from media.widgets import DocumentSelectMultiple, GallerySelectMultiple, ImageSelectMultiple


class DocumentMultipleChoiceField(ModelMultipleChoiceField):
    """ModelMultipleChoiceField select field with ajax document picker."""
    widget = DocumentSelectMultiple()


class GalleryMultipleChoiceField(ModelMultipleChoiceField):
    """ModelMultipleChoiceField select field with ajax gallery picker."""
    widget = GallerySelectMultiple()


class ImageMultipleChoiceField(ModelMultipleChoiceField):
    """ModelMultipleChoiceField select field with ajax image picker."""
    widget = ImageSelectMultiple()

