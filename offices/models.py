from django.db import models
from django.contrib.auth import get_user_model
from zones.models import Zone
from zones.pivot_table import OfficeZoneMapping

AuthUserModel = get_user_model()


class Office(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    zone = models.ManyToManyField(Zone, through=OfficeZoneMapping)
    # office_location = models.IntegerField(choices=[(x, str(x)) for x in range(1, 48)])
    owner = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False)
    # date_from = models.DateTimeField(verbose_name=_('From'), blank=True, null=True,)
    # date_until = models.DateTimeField(verbose_name=_('Until'), blank=True, null=True,)

    def __str__(self):
        return f'<Office object ID = {self.id}>'
