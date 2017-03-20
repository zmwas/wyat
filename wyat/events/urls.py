from django.conf.urls import include,url


from rest_framework_nested import routers

from events.views import EventActivtiesViewSet
from .views import EventViewSet,VenueViewSet

router = routers.SimpleRouter()


router.register(r'venues',VenueViewSet,base_name="venues")
router.register(r'events',EventViewSet,base_name="events")

activities_router = routers.NestedSimpleRouter(router,r'events',lookup='event')
activities_router.register(r'activities',EventActivtiesViewSet,base_name='event-activities')

urlpatterns = [

    url(r'',include(router.urls)),
    url(r'',include(activities_router.urls))



]