from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify


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


def generate_unique_image_slug(text, iteration=0):
    """Generate a unique slug for an image from the provided text."""
    from thecut.media.models import Image
    queryset = Image.objects
    slug = slugify(text)
    if iteration > 0:
        slug = '%s-%s' %(iteration, slug)
    slug = slug[:50]
    try:
        queryset.get(title_slug=slug)
    except Image.DoesNotExist:
        return slug
    else:
        iteration += 1
        return generate_unique_slug(text, iteration=iteration)

