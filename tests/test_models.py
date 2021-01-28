from django.test import TestCase

from staff.models import Staff, Device


class StaffModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Staff.objects.create(first_name='Alex', last_name='Zubritskiy', phone_number='1234567', team='TMS')

    def test_first_name_label(self):
        staff = Staff.objects.get(id=1)
        field_label = staff._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'First name')

    def test_last_name_label(self):
        staff = Staff.objects.get(id=1)
        field_label = staff._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Last name')

    def test_phone_number_label(self):
        staff = Staff.objects.get(id=1)
        field_label = staff._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'Phone number')

    def test_team_label(self):
        staff = Staff.objects.get(id=1)
        field_label = staff._meta.get_field('team').verbose_name
        self.assertEquals(field_label, 'Team')

    def test_first_name_max_length(self):
        staff = Staff.objects.get(id=1)
        max_length = staff._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_label_max_length(self):
        staff = Staff.objects.get(id=1)
        max_length = staff._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_phone_number_label_max_length(self):
        staff = Staff.objects.get(id=1)
        max_length = staff._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 30)

    def test_team_label_max_length(self):
        staff = Staff.objects.get(id=1)
        max_length = staff._meta.get_field('team').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_and_first_name_andphone_number_and_team(self):
        staff = Staff.objects.get(id=1)
        expected_object_name = '%s, %s, %s, %s' % (staff.last_name, staff.first_name, staff.phone_number, staff.team)
        self.assertEquals(expected_object_name, str(staff))

    def test_get_absolute_url(self):
        staff = Staff.objects.get(id=1)
        self.assertEquals(staff.get_absolute_url(), '/test_task/staff/1')


class DeviceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Device.objects.create(type_of_device='Headpones ',  name_of_device ='xiaomi',

                              configuration ='https://xiaomi-store.by/catalog/naushniki',

                              paid_by="Sergei"
                              )

    def test_type_of_device_label(self):
        device = Device.objects.get(id=1)
        field_label = device._meta.get_field('type_of_device').verbose_name
        self.assertEquals(field_label, 'Type')

    def test_name_of_device_label(self):
        device = Device.objects.get(id=1)
        field_label = device._meta.get_field('name_of_device').verbose_name
        self.assertEquals(field_label, 'Device name')

    def test_configuration_label(self):
        device = Device.objects.get(id=1)
        field_label = device._meta.get_field('configuration').verbose_name
        self.assertEquals(field_label, 'Link')

    def test_paid_by_label(self):
        device = Device.objects.get(id=1)
        field_label = device._meta.get_field('paid_by').verbose_name
        self.assertEquals(field_label, 'Buyer')

    def test_type_of_device_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('type_of_device').max_length
        self.assertEquals(max_length, 50)

    def test_name_of_device_label_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('name_of_device').max_length
        self.assertEquals(max_length, 50)

    def test_paid_by_label_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('paid_by').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        device = Device.objects.get(id=1)
        expected_object_name = '%s, %s, %s, %s' % (device.type_of_device, device.name_of_device, device.configuration, device.paid_by)
        self.assertEquals(expected_object_name, str(device))

    def test_get_absolute_url(self):
        device = Device.objects.get(id=1)
        self.assertEquals(device.get_absolute_url(), '/test_task/device/1')
