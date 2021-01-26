
from api.views import StaffViewSet, DeviceViewSet,DeliveryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"staff", StaffViewSet)
router.register(r"device", DeviceViewSet)
router.register(r"delivery", DeliveryViewSet)

urlpatterns = router.urls