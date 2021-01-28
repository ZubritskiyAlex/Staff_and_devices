from django.test import TestCase

from staff.models import Staff, Device

from api.serializers import StaffSerializer, DeviceSerializer


class StaffSerializerTest(TestCase):
    def setUp(self):
        self.staff_attributes = {
            "first_name": "Alex",
            "last_name": "Zubritskiy",
            "phone_number": "1234567",
            "team": "TMS"
        }

        self.serializer_data = {
            "first_name": "Zeka",
            "last_name": "Petuhov",
            "phone_number": "7654321",
            "team": "EPAM"
        }

        self.staff = Staff.objects.create(**self.staff_attributes)
        self.serializer = StaffSerializer(instance=self.staff, context={'request': None})

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"first_name", "last_name", "photo", "phone_number", "id", "team", 'url'})

    def test_first_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["first_name"], self.staff_attributes["first_name"])

    def test_last_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["last_name"], self.staff_attributes["last_name"])

    def test_phone_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["phone_number"], self.staff_attributes["phone_number"])

    def test_team_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["team"], self.staff_attributes["team"])


class DeviceSerializerTest(TestCase):
    def setUp(self):
        self.device_attributes = {
            "type_of_device": "Headpones",
            "name_of_device": "Xiaomi",
            "configuration": "https://xiaomi-store.by/catalog/naushniki",
            "price": 87,
            "paid_by": "Sergei",
            "item_number": 5,
        }

        self.serializer_data = {
            "type_of_device": "laptop",
            "name_of_device": "Xiaomi ",
            "configuration": "https://xiaomi-store.by/catalog/noutbuki/noutbuk-xiaomi-redmibook-14",
            "price": 115,
            "paid_by":"Sergei",
            "item_number": 7,
        }

        self.device = Device.objects.create(**self.device_attributes)
        self.serializer = DeviceSerializer(instance=self.device, context={'request': None})

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"type_of_device", "name_of_device", "configuration", "price", "staff_start_date", "price"})

    def test_device_type_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["type_of_device"], self.device_attributes["type_of_device"])

    def test_device_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name_of_device"], self.device_attributes["name_of_device"])

    def test_device_model_content(self):
        data = self.serializer.data
        self.assertEqual(data["configuration"], self.device_attributes["configuration"])

    def test_price_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["price"], self.device_attributes["price"])

    def test_paid_by_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["paid_by"], self.device_attributes["paid_by"])

    def test_item_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["item_number"], self.device_attributes["item_number"])
