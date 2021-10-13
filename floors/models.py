from django.db import models
from django.contrib.auth import get_user_model
from utils import F1, F2

AuthUserModel = get_user_model()


class Floor(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    floor_levels = models.CharField(choices=((F1, 'F1'), (F2, 'F2')), max_length=2)

    def __str__(self):
        return f'<Floor object ID = {self.id}>'
