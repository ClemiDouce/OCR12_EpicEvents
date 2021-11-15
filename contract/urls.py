from rest_framework.routers import DefaultRouter

from contract.views import ContractViewset

router = DefaultRouter()
router.register("contracts", ContractViewset, basename="contracts")

urlpatterns = router.urls