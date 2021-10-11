from django.db import models
from django.contrib.auth import get_user_model
from utils.constants.zone_location import ZONE_LOCATION
from floors.models import Floor


AuthUserModel = get_user_model()


class Zone(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    floor = models.ForeignKey(Floor, related_name='floor', on_delete=models.CASCADE, default=None, null=True)
    zone_location = models.CharField(choices=ZONE_LOCATION, max_length=20)

    def __str__(self):
        return f'<Zone object ID = {self.id}>'
