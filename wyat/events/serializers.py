from actstream.signals import action
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework_nested.relations import NestedHyperlinkedIdentityField, NestedHyperlinkedRelatedField

from .models import Event, Venue
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


class VenueSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Venue
        geo_field = "point"
        fields = ('id', 'address', 'city', 'rating')



class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(many=False, read_only=True)

    thumbnail = HyperlinkedSorlImageField(
            '128x128',
            options={"crop": "center"},
            source='event_pic_url',
            read_only=True
    )
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    venue_id = serializers.PrimaryKeyRelatedField(queryset=Venue.objects.all(), source='venue', write_only=True)

    # A larger version of the image, allows writing
    event_pic_url = HyperlinkedSorlImageField('1024')


    class Meta:
        model = Event
        fields = '__all__'





    def create(self, validated_data):
        user = serializers.CurrentUserDefault()

        event = Event.objects.create()
        action.send(user, verb="added", action_object=event)

        return event
