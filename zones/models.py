from django.db import models
from django.contrib.auth import get_user_model
from floors.models import Floor
from utils.constants.zone_location import Z1,Z2,Z3,Z4
from utils.constants.zone_equipment import P,K,R
from zones.pivot_table import FloorZoneMapping


AuthUserModel = get_user_model()


class Zone(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    floor = models.ManyToManyField(Floor, through=FloorZoneMapping)
    zone_equipment = models.CharField(choices=((P, 'P'), (K, 'K'), (R, 'R')), max_length=1)
    zone_location = models.CharField(choices=((Z1, 'Z1'), (Z2, 'Z2'), (Z3, 'Z3'), (Z4, 'Z4')), max_length=2)

    def __str__(self):
        return f'<Zone object ID = {self.id}>'



