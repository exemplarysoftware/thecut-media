from django.forms import ModelMultipleChoiceField
from media.widgets import ImageSelectMultiple


class ImageMultipleChoiceField(ModelMultipleChoiceField):
    """ModelMultipleChoiceField select field with ajax image picker."""
    widget = ImageSelectMultiple()

