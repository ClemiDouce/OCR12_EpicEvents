from rest_framework.routers import DefaultRouter

from client.views import ClientViewset
from contract.views import ContractViewset
from event.views import EventViewset

router = DefaultRouter()
router.register("clients", ClientViewset, basename="clients")
router.register(r"clients/(?P<client_id>[^/.]+)/contracts", ContractViewset, basename="contracts")
router.register(r"clients/(?P<client_id>[^/.]+)/events", EventViewset, basename="events")

urlpatterns = router.urls