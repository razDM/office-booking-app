from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from utils import F1, F2, F3, F4
from utils.constants.zone_location import ZONE_LOCATION


AuthUserModel = get_user_model()


class Floor(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    floor_levels = models.CharField(choices=((F1, 'F1'), (F2, 'F2'), (F3, 'F3'), (F4, 'F4')), max_length=2)

    def __str__(self):
        return f'{self.id}'


class Zone(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    floor = models.ForeignKey(Floor, related_name='floor', on_delete=models.CASCADE, default=None, null=True)
    zone_location = models.CharField(choices=ZONE_LOCATION, max_length=20)

    def __str__(self):
        return f'{self.id}'


class Office(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    zone = models.ForeignKey(Zone, related_name='zone', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.id}'

