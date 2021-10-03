from django.db import models
from django.contrib.auth import get_user_model
from models.zones import Zone
# from models.office_zone import OfficeZoneMapping


AuthUserModel = get_user_model()


class Office(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'<Office object ID = {self.id}>'
