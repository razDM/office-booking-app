import datetime

from django.contrib import messages
from django.shortcuts import redirect

from selection.models import Office
from offices.models import Reservation
import time
import datetime


def get_valid_dates(request, req_start_date, req_end_date):
    user_reservations = list(Reservation.objects.filter(user_id=request.user).values())

    for booking in user_reservations:
        #get overlap of periods.
        if (booking['start_date'] <= datetime.datetime.strptime(req_start_date,'%Y-%m-%d').date() <=
            booking['end_date']) or \
                (datetime.datetime.strptime(req_start_date,'%Y-%m-%d').date() <= booking['start_date'] <=
                    datetime.datetime.strptime(req_end_date,'%Y-%m-%d').date()):
            messages.warning( request, 'Please Do not overlap periods' )
            redirect('/')
            return False
    return True


def check_availability(reservation, start_date, end_date):
    avail_list = []
    reservation_list = list(Reservation.objects.filter(office_id=reservation).values())
    start_y, start_m, start_d = (int(start_date.split('-')[0]), int(start_date.split('-')[1]), int(start_date.split('-')[2]))
    end_y, end_m, end_d = (int(end_date.split('-')[0]), int(end_date.split('-')[1]), int(end_date.split('-')[2]))

    for reservation in reservation_list:

        if reservation['start_date'] > datetime.date(end_y, end_m, end_d) or reservation['end_date'] < datetime.date(start_y, start_m, start_d):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)


