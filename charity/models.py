from django.contrib.auth.models import User
from django.db import models

from charity.constants import Institutions


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        self.name


class Institution(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField
    type = models.PositiveSmallIntegerField(choices=Institutions.Choices, default=Institutions.Choices[0][0])
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.SmallIntegerField
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=56)
    city = models.CharField(max_length=56)
    zip_code = models.CharField(max_length=56)
    pick_up_date = models.DateField
    pick_up_time = models.TimeField
    pick_up_comment = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
