from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from selection.models import Office
from django.urls import reverse_lazy




AuthUserModel = get_user_model()


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, default=None, related_name='office')
    start_date = models.DateField()
    end_date = models.DateField()

    @property
    def is_past_due(self):
        return date.today() > self.start_date

    class Meta:
        unique_together = (('user', 'office', 'start_date', 'end_date'),
                           ('user', 'start_date', 'end_date')
                           )
