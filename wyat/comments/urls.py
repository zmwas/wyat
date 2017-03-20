from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from comments.views import CommentsViewSet

router = DefaultRouter()
router.register(r'comments', CommentsViewSet, base_name="comments")

urlpatterns = [

    url(r'', include(router.urls))

]
