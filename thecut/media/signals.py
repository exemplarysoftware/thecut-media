from datetime import datetime


def set_publish_at(sender, instance, **kwargs):
    """If not already set, automatically set the instance's publish_at value to now."""
    instance.publish_at = instance.publish_at or datetime.now()

