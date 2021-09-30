from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.constants.gender_choices import GENDER_CHOICES


class User(AbstractUser):
    is_warden = models.BooleanField(default=False)


class Employee:
    name = models.CharField( max_length=128, unique=False, null=False )
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default=None, null=True )

    def __str__(self):
        return f'<User object ID = {self.id}>'
