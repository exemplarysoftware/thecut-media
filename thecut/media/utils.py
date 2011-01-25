from django.contrib.contenttypes.models import ContentType


def get_mediaset(instance):
    """Returns MediaSet for the instance provided."""
    from thecut.media.models import MediaSet
    content_type = ContentType.objects.get_for_model(instance)
    try:
        media = MediaSet.objects.get(content_type=content_type,
        object_id=instance.id)
    except MediaSet.DoesNotExist:
        media = None
    return media


@property
def media(self):
    """Property for adding to classes - returns MediaSet instance."""
    return get_mediaset(instance=self)

