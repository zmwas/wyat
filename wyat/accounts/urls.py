from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


from .views import UserViewSet

router = routers.DefaultRouter()

router.register(r'users',UserViewSet,base_name="users")

urlpatterns = [



    url(r'',include(router.urls)),


]