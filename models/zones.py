from django.db import models
from django.contrib.auth import get_user_model
from utils.constants import zone_location
from models.floors import Floor


AuthUserModel = get_user_model()


ZONE_LOCATION= [
    ('Z1', 'Zone one'),
    ('Z2', 'Zone two'),
    ('Z3', 'Zone three'),
    ('Z4','Zone four'),
    ('Z5','Zone five'),
    ('Z6', 'Zone six'),
    ('Z7', 'Zone seven'),
    ('Z8', 'Zone eight'),
]
class Zone(models.Model):
    name = models.CharField(max_length=128, unique=False, null=False)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, default=None, null=True)
    zone_location = models.CharField(choices=ZONE_LOCATION, max_length=20)

    def __str__(self):
        return f'<Zone object ID = {self.id}>'
