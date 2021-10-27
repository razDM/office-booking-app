import datetime
from selection.models import Office
from offices.models import Reservation
import time


def check_availability(reservation, start_date, end_date):
    avail_list = []
    reservation_list = list(Reservation.objects.filter(office_id=reservation).values())
    start_y,start_m,start_d = (int(start_date.split('-')[0]),int(start_date.split('-')[1]),int(start_date.split('-')[2]))
    end_y,end_m,end_d = (int(end_date.split('-')[0]),int(end_date.split('-')[1]),int(end_date.split('-')[2]))

    for reservation in reservation_list:
        if reservation['start_date'] > datetime.date(end_y, end_m, end_d) or reservation['end_date'] < datetime.date(start_y,start_m,start_d):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
