from django.db import models

# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    photo = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(verbose_name="Phone")
    team = models.CharField(max_length=50,verbose_name="Team")
    db_table = models.CharField(max_length=200,verbose_name="Name of table")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "Staff"


class Device(models.Model):
    type_of_device = models.CharField(max_length= 50,verbose_name="Type")
    name_of_device = models.CharField(max_length= 50, verbose_name="Device name")
    configuration = models.URLField(verbose_name="Link")
    price = models.IntegerField()
    paid_by = models.CharField(max_length=50,verbose_name="Buyer")
    item_number = models.IntegerField()
    db_table = models.CharField(max_length=200, verbose_name="Name of table")

    def __str__(self):
        return self.name_of_device


class Delivery(models.Model):
    person = models.ForeignKey(Staff, on_delete=models.PROTECT)
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    comment = models.TextField(null=True, blank=True)
    delivery_date = models.DateField(auto_now=True)
    db_table = models.CharField(max_length=200, verbose_name="Name of table")


    class Meta:
        db_table = "Delivery"

    def __str__(self):
        return f"{self.person} {self.device}"