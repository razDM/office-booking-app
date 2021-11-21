from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.utils import timezone

from selection.models import Department
from utils.constants.activation import ACTIVATION_DICT

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default=None)
    department = models.ForeignKey(Department, related_name='department_id', on_delete=models.CASCADE, default=None, null=True)

    @property
    def image(self):
        if self.avatar:
            return self.avatar.url

        return static('images/defaultUser.jpg')


class Activation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activation')
    token = models.CharField(max_length=64, null=True, default=None, blank=False, unique=True)
    expires_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(**ACTIVATION_DICT))
    activated_at = models.DateTimeField(null=True, default=None, blank=False)

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token
