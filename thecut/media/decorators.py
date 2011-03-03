from functools import partial
from thecut.media.utils import get_mediaset_for_object


def attach_mediaset(obj):
    obj.media = property(partial(get_mediaset_for_object))
    return obj

