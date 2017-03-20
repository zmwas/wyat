from rest_framework import viewsets

from .serializers import AlbumSerializer,PhotoSerializer
from  .models import Album,Photo



class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

