from django.contrib import messages
from django.shortcuts import redirect
from selection.models import Office
from offices.models import Reservation
from datetime import datetime


def is_overlap(request, req_start_date, req_end_date):
    user_reservations = list(Reservation.objects.filter(user_id=request.user).values())

    for booking in user_reservations:
        if (booking['start_date'] <= datetime.strptime(req_start_date, '%Y-%m-%d').date() <=
            booking['end_date']) or \
                (datetime.strptime(req_start_date, '%Y-%m-%d').date() <= booking['start_date'] <=
                    datetime.strptime(req_end_date, '%Y-%m-%d').date()):
            return False
    return True


def check_availability(reservation, start_date, end_date):
    start_y, start_m, start_d = (int(start_date.split('-')[0]),
                                 int(start_date.split('-')[1]),
                                 int(start_date.split('-')[2]))
    end_y, end_m, end_d = (int(end_date.split('-')[0]), int(end_date.split('-')[1]), int(end_date.split('-')[2]))
    booked_offices = Reservation.objects.filter(end_date__gte=datetime(start_y, start_m, start_d), start_date__lte=datetime(end_y, end_m, end_d)).values_list('office_id', flat=True)
    return Office.objects.exclude(id__in=booked_offices)

