from __future__ import unicode_literals


from actstream import action
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import post_save
from stream_framework.activity import Activity
from stream_framework.verbs.base import Add
from accounts.models import User
from comments.models import Comment
from events.models import Event



# Create your models here.
class Album(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event,blank=True,null=True)
    title = models.CharField(max_length=254)
    tags = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event, blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True)
    name = models.CharField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="pictures/%Y%m%d/")
    comments = GenericRelation(Comment)
    created_at = models.DateTimeField(auto_now_add=True)




def photo_activity(sender, instance,created, **kwargs):
    if created:
       action.send(instance.user, verb='posted a photo on', action_object=instance, target=instance.event)


post_save.connect(photo_activity, sender=Photo, dispatch_uid=photo_activity)

