from django.conf.urls import include,url


from rest_framework_nested import routers

from events.views import EventActivtiesViewSet, EventPhotosViewSet
from .views import EventViewSet,VenueViewSet

router = routers.SimpleRouter()


router.register(r'venues',VenueViewSet,base_name="venues")
router.register(r'events',EventViewSet,base_name="events")

nested_router = routers.NestedSimpleRouter(router,r'events',lookup='event')
nested_router.register(r'activities',EventActivtiesViewSet,base_name='event-activities')
nested_router.register(r'photos',EventPhotosViewSet,base_name='event-photos')


urlpatterns = [

    url(r'',include(router.urls)),
    url(r'',include(nested_router.urls))



]