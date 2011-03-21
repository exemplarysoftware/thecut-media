from django.conf import settings


def get_media_source_classes(model_list=None):
    """Returns classes for the each string in list."""
    from thecut.media.models import AbstractMediaItem
    model_list = model_list or getattr(settings, 'MEDIA_SOURCES', [])
    source_classes = []
    for import_string in model_list:
        module_string = '.'.join(import_string.split('.')[:-1])
        class_string = import_string.split('.')[-1]
        module = __import__(module_string, globals(), locals(), [class_string])
        class_ = getattr(module, class_string)
        if issubclass(class_, AbstractMediaItem):
            source_classes += [class_]
    return source_classes

