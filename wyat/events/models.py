import pytz

from django.contrib.contenttypes.fields import GenericRelation

from comments.models import Comment


from django.contrib.gis.db.models.manager import GeoManager
from accounts.models import User
from django.contrib.gis.db import models


# Create your models here.




class Venue(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    point = models.PointField(null=True, max_length=40)

    objects = GeoManager()


class Event(models.Model):
    EVENT_TYPE = (('Movie', 'Movie'), ('Concert', 'Concert'), ('Conference', 'Conference'), ('Festival', 'Festival'),
                  ('Wedding', 'Wedding'), ('Party', 'Party'))
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event_pic_url = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    venue = models.ForeignKey(Venue)
    description = models.TextField(default='Please add a description')
    event_type = models.CharField(max_length=100, choices=EVENT_TYPE)
    invite_only = models.BooleanField(default=False)
    free = models.BooleanField(default=True)
    age_restriction = models.BooleanField(default=False)
    ticket_price = models.FloatField(max_length=4, blank=True, null=True)
    comments = GenericRelation(Comment)
    created_at = models.DateTimeField(auto_now_add=True)
