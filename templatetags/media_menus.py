from django import template
from media.models import Gallery


register = template.Library()


@register.inclusion_tag('media/_gallery_menu.html', takes_context=True)
def gallery_menu(context, path=None):
    """Gallery menu (un-ordered list)."""
    if path is None:
        path = context['request'].path
    gallery_list = Gallery.objects.current_site().active()
    return {'gallery_list': gallery_list, 'path': path}

