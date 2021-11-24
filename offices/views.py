from datetime import datetime, time
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .booking_functions.reservation_details import office_zone_details
from .forms import AvailabilityForm
from django.http import HttpResponse
from django.db import IntegrityError
from offices.models import Reservation
from offices.booking_functions.availability import check_availability, get_valid_dates
from selection.models import Office, Zone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages

AuthUserModel = get_user_model()


def get_available_offices(request):
    if request.method == 'GET' and len(request.GET) > 0:

        if request.GET['start_date'] < datetime.strftime(datetime.now(),'%Y-%m-%d'):
            print(request.GET['start_date'],datetime.strftime(datetime.now(),'%Y-%m-%d'),'First IF')
            messages.warning( request, 'The enter date must be grater than today' )
            return redirect('/')
        if request.GET['start_date'] > request.GET['end_date']:
            messages.warning( request, 'Start Date must be grater than endate' )
            return redirect('/')
        if not get_valid_dates(request, request.GET['start_date'], request.GET['end_date']):
            messages.warning(request, 'Do not overlap periods' )
            return redirect('/')

        offices_for_booking = check_availability(request, request.GET['start_date'], request.GET['end_date'])

        return render( request, 'offices/availability.html',
                       {'form_data': offices_for_booking,
                        'start_date': request.GET['start_date'],
                        'end_date': request.GET['end_date']})
    else:
        messages.warning(request, 'Something went wrong')
        return redirect('/')


def book_now(request, id, start_date, end_date):
    office_to_book = Office.objects.get(id=id)
    return render(request, 'offices/reservation.html', {'office_to_book': office_to_book,
                                                        'start_date': start_date, 'end_date': end_date})


def save_booking(request, id, start_date, end_date):
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
                'You have successfully reserved ' f'{office_obj.name}',
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
    bookings = Reservation.objects.filter(start_date__gte=datetime.strftime(datetime.now(),'%Y-%m-%d'), user=request.user)
    return render(request, 'offices/bookings.html',
                  {'user_bookings': bookings})


def cancel_booking(request, id):
    try:
        Reservation.objects.filter(id=id).delete()
        return redirect('/')
    except Exception as ex:
        return(HttpResponse(status=400))
