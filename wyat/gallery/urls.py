from django.conf.urls import url, include

from rest_framework import routers

from .views import AlbumViewset,PhotoViewSet


router = routers.DefaultRouter()

router.register(r'albums',AlbumViewset,base_name="albums")
router.register(r'photos',PhotoViewSet,base_name="photos")


urlpatterns = [


    url(r'',include(router.urls))


]

