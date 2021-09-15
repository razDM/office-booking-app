from django.db import models
from django.contrib.auth import get_user_model
from utils import WSD, WDD, ISD, IDD
from utils import D, P
from utils import X, K, R

AuthUserModel = get_user_model()


class Floor(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    floor_equipment = models.CharField(choices=((X, 'X'), (K, 'K'), (R, 'R')), max_length=1)

    def __str__(self):
        return f'<Floor office ID = {self.id}>'


class Office(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    floor = models.ManyToManyField(Floor, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False)
    office_equipment = models.CharField(choices=((D, 'D'), (P, 'D')), max_length=1)
    office_location = models.CharField(choices=((WSD, 'wsd'), (WDD, 'wdd'), (ISD, 'isd'), (IDD, 'idd')), max_length=3)
    owner = models.OneToOneField(AuthUserModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'<Office ID = {self.id}>'
