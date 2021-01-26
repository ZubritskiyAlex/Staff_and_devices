from django.contrib import admin
from staff.models import Staff, Device, Delivery

# Register your models here.

# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('first_name','last_name','photo', 'phone_number')
#
# @admin.register(Device)
# class DeviceAdmin(admin.ModelAdmin):
#     list_display = ('type_of_device','name_of_device','configuration',
#
#                     'price', 'paid_by','used_by','team',
#
#                     'comment','item_number','employee_start_date')

admin.site.register(Staff)
admin.site.register(Device)
admin.site.register(Delivery)