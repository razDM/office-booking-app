from datetime import datetime

from django.shortcuts import render, get_object_or_404, reverse, redirect

from .booking_functions.reservation_details import office_zone_details
from .forms import AvailabilityForm
from django.http import HttpResponse
from django.db import IntegrityError
from offices.models import Reservation
from offices.booking_functions.availability import check_availability
from selection.models import Office, Zone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

AuthUserModel = get_user_model()


def get_available_offices(request):
    if request.method == 'GET' and len(request.GET) > 0:
        offices = list(Office.objects.values())
        available_offices = []
        for office in offices:
            if check_availability(office['id'], request.GET['start_date'], request.GET['end_date']):
                available_offices.append(office)
    else:
        form = AvailabilityForm()
    return render(request, 'offices/availability.html',
                {'form_data': available_offices,
                 'start_date': request.GET['start_date'],
                 'end_date': request.GET['end_date']})


def book_now(request, id, start_date, end_date):
    office_details, zone_details = office_zone_details(id)
    return render(request, 'offices/reservation.html', {'office_details': office_details, 'zone_details': zone_details,
                                                        'start_date': start_date, 'end_date': end_date})


def do_booking(request, id, start_date, end_date):
    if request.method == 'POST':
        try:
            office_obj = Office.objects.get(id=id)
            Reservation.objects.create(
                user=request.user,
                office=office_obj,
                start_date=start_date,
                end_date=end_date
            )
            send_mail(
                'Office booking confirmation',
                'You have succesfully reserverd ' f'{office_obj.name}',
                'razvan1989@gmail.com',
                [request.user.email],
            )
        except IntegrityError as e:
            return HttpResponse(status=400)
        return redirect('/')


def back_button(request):
    if request.method == 'POST':
        return redirect('/')


def my_bookings(request):

    bookings = Reservation.objects.filter(start_date__gte='2021-11-19')
    my_bookings = bookings.filter(user=request.user)
    booking_info = {}
    booking_list = []
    for booking in list(my_bookings.values()):
        office_details, zone_details = office_zone_details(booking['office_id'])
        booking_info['Office'] = office_details
        booking_info['Zone'] = list(zone_details.values())[0]['name']
        booking_info['Floor'] = list(zone_details.values())[0]['floor_id']

        booking_info['Start Date'] = booking['start_date']
        booking_info['End Date'] = booking['end_date']
        booking_info['BookingId'] = booking['id']
        booking_list.append(booking_info.copy())
    return render(request, 'offices/bookings.html', {
        'my_bookings': booking_list,

    })

def cancel_booking(requeset,id):
    print(id)
    try:
        Reservation.objects.filter(id=id).delete()
        return(HttpResponse(status=201))
    except Exception as ex:
        return(HttpResponse(status=400))
