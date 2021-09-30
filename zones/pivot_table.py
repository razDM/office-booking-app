from django.db import models
from offices.models import Office
from zones.models import Zone
from floors.models import Floor
from datetime import datetime


class OfficeZoneMapping(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=datetime.now)


class FloorZoneMapping(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=datetime.now)
