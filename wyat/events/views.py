from actstream.models import Action, target_stream

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from newsfeed.serializers import ActionSerializer

from .serializers import EventSerializer, VenueSerializer
from .models import Event, Venue


# Create your views here.
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventActivtiesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActionSerializer
    queryset = Action.objects.all()

    def list(self, request, event_pk=None):
        event = get_object_or_404(Event.objects.all(), pk=event_pk)

        qs = target_stream(event)

        serializer = ActionSerializer(qs, many=True)

        return Response(serializer.data)
