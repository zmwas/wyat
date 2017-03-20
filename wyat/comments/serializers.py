from django.apps.config import AppConfig
from django.apps import apps

from generic_relations.serializers import GenericModelSerializer
from rest_framework import serializers

from comments.models import Comment
from events.serializers import EventSerializer
from events.models import Event
from gallery.models import  Photo
from gallery.serializers import  PhotoSerializer


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'














