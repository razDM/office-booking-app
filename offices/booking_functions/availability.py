from django.contrib import messages
from django.shortcuts import redirect
from selection.models import Office
from offices.models import Reservation
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
    start_y, start_m, start_d = (int( start_date.split( '-' )[0] ), int( start_date.split( '-' )[1] ), int( start_date.split( '-' )[2] ))
    end_y, end_m, end_d = (int( end_date.split( '-' )[0] ), int( end_date.split( '-' )[1] ), int( end_date.split( '-' )[2] ))
    availible_offices = Reservation.objects.filter(end_date__gte=datetime.datetime(start_y,start_m,start_d),start_date__lte=datetime.datetime(end_y,end_m,end_d)).values()
    list_of_exclusion = []
    for office_to_add in availible_offices:
        list_of_exclusion.append(office_to_add['office_id'])
    return Office.objects.exclude(id__in=list_of_exclusion)

