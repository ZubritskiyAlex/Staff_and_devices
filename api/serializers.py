from rest_framework import serializers

from staff.models import Staff, Device, Delivery

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"

class DeliverySerializer(serializers.ModelSerializer):
    person = StaffSerializer()
    device = DeviceSerializer()

    class Meta:
        model = Delivery
        fields = ("person", "device", "comment")
