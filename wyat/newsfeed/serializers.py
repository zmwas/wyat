from actstream.models import Action
from rest_framework import serializers
from accounts.models import User
from accounts.serializers import UserSerializer
from events.models import Event
from gallery.models import Album,Photo



from events.serializers import EventSerializer
from gallery.serializers import PhotoSerializer,AlbumSerializer


class GenericRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value,Album):
            return AlbumSerializer(value).data
        elif isinstance(value,Event):
            return EventSerializer(value).data
        elif isinstance(value,Photo):
            return PhotoSerializer(value).data
        elif isinstance(value,User):
            return UserSerializer(value).data




class ActionSerializer(serializers.ModelSerializer):
    actor = GenericRelatedField(read_only=True)
    target = GenericRelatedField(read_only=True)
    action_object = GenericRelatedField(read_only=True)


    class Meta:
        model = Action
        fields = ('id','actor','verb','action_object','target')
