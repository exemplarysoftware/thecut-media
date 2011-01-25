from thecut.media.utils import media as mediaset


def attach_mediaset(obj):
    obj.media = mediaset
    return obj

