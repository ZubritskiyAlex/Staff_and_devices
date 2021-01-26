from rest_framework.viewsets import ModelViewSet
from api.serializers import StaffSerializer,DeviceSerializer,DeliverySerializer
from staff.models import Staff, Device, Delivery


class StaffViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

class DeviceViewSet(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

class DeliveryViewSet(ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()

