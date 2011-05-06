import warnings


def attach_mediaset(obj):
    """Deprecated. Media is now added to AbstractResource."""
    warnings.warn('Media is now directly added to the AbstractResource'
        'class.', DeprecationWarning, stacklevel=2)
    return obj

