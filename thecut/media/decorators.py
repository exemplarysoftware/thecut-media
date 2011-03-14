from django.contrib.contenttypes.generic import GenericRelation


def attach_mediaset(obj):
    obj.add_to_class('media', GenericRelation(
        'media.AttachedMediaItem',
        content_type_field='parent_content_type',
        object_id_field='parent_object_id'))
    return obj

