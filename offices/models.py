from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from selection.models import Office
from django.urls import reverse_lazy


AuthUserModel = get_user_model()


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, default=None, related_name='office')
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return f'{self.user} has booked {self.office} from {self.start_date.strftime("%d-%b-%Y %H:%M")} to' \
    #            f' {self.end_date.strftime("%d-%b-%Y %H:%M")} '

    # def get_cancel_reservation_url(self):
    #     return reverse_lazy('offices:CancelReservationView', args=[self.pk, ])
