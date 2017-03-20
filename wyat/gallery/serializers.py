from actstream.signals import action
from rest_framework import serializers
from .models import Album, Photo

from events.serializers import EventSerializer

from events.models import Event

from accounts.serializers import UserSerializer

from sorl.thumbnail import get_thumbnail


class HyperlinkedSorlImageField(serializers.ImageField):

    """A Django REST Framework Field class returning hyperlinked scaled and cached images."""

    def __init__(self, geometry_string, options={}, *args, **kwargs):
        """
        Create an instance of the HyperlinkedSorlImageField image serializer.
        Args:
            geometry_string (str): The size of your cropped image.
            options (Optional[dict]): A dict of sorl options.
            *args: (Optional) Default serializers.ImageField arguments.
            **kwargs: (Optional) Default serializers.ImageField keyword
            arguments.
        For a description of sorl geometry strings and additional sorl options,
        please see https://sorl-thumbnail.readthedocs.org/en/latest/examples.html?highlight=geometry#low-level-api-examples
        """  # NOQA
        self.geometry_string = geometry_string
        self.options = options

        super(HyperlinkedSorlImageField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        """
        Perform the actual serialization.
        Args:
            value: the image to transform
        Returns:
            a url pointing at a scaled and cached image
        """
        if not value:
            return None

        image = get_thumbnail(value, self.geometry_string, **self.options)

        try:
            request = self.context.get('request', None)
            return request.build_absolute_uri(image.url)
        except:
            try:
                return super(HyperlinkedSorlImageField, self).to_representation(image.url)
            except AttributeError:  # NOQA
                return super(HyperlinkedSorlImageField, self).to_native(image.url)  # NOQA
    to_native = to_representation



class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "event", "title", "tags", "user"]

    def create(self, validated_data):
        album = Album(
                user=self.context['request'].user,
                event=validated_data['event'],
                title=validated_data['title'],
                tags=validated_data['tags']

        )

        album.save()


class PhotoSerializer(serializers.ModelSerializer):

    album= AlbumSerializer(many=False,read_only=True)
    event = EventSerializer(many=False,read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), source='event', write_only=True)
    album_id=serializers.PrimaryKeyRelatedField(queryset=Album.objects.all(), source='album', write_only=True,required=False)


    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )


    class Meta:
        model = Photo
        fields = ["id", "event", "album", "name", "timestamp", "photo", "user",'thumbnail','event_id','album_id']



    def create(self,validated_data):
        user = self.context['request'].user
        validated_data.pop('user')

        photo = Photo.objects.create(user= user,**validated_data)

        action.send(user,verb="added",action_object=photo,target=photo.event)


        return photo
