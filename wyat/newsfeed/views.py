from actstream.models import Action, target_stream
from rest_framework import viewsets
# Create your views here.

from newsfeed.serializers import ActionSerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


