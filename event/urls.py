from rest_framework.routers import DefaultRouter

from event.views import EventViewset

router = DefaultRouter()
router.register("events", EventViewset, basename="events")

urlpatterns = router.urls
