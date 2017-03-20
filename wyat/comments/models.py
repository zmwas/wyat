from __future__ import unicode_literals

from actstream import action
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from accounts.models import User


class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


def comment_activity(sender, instance,created, **kwargs):
    if created:
       action.send(instance.user, verb='commented on', action_object=instance, target=instance.content_object)


post_save.connect(comment_activity, sender=Comment, dispatch_uid=comment_activity)
