from django.conf.urls import url, include

from rest_framework import routers

from .views import ActivityViewSet

router = routers.DefaultRouter()


router.register(r'activities',ActivityViewSet,base_name='activities')


urlpatterns = [


    url(r'',include(router.urls)),


]
