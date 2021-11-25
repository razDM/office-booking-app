from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from offices.models import Reservation
from offices.booking_functions.availability import check_availability, is_overlap
from selection.models import Office, Floor, Zone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib import messages
from django.core.cache import cache

AuthUserModel = get_user_model()


def get_available_offices(request):
    if request.method == 'GET' and len(request.GET) > 0:
        if request.GET['start_date'] < datetime.strftime(datetime.now(), '%Y-%m-%d'):
            messages.warning(request, 'The enter date must be grater than today')
            return redirect('/')
        if request.GET['start_date'] > request.GET['end_date']:
            messages.warning(request, 'Start Date must be grater than end date')
            return redirect('/')
        if not is_overlap(request, request.GET['start_date'], request.GET['end_date']):
            messages.warning(request, 'Please Do not overlap periods')
            return redirect('/')
        offices_for_booking = check_availability(request, request.GET['start_date'], request.GET['end_date'])
        offices_for_booking_cache = cache.get(request.session.session_key)
        request.session['start_date'] = request.GET['start_date']
        request.session['end_date'] = request.GET['end_date']

        if not offices_for_booking_cache:
            cache.set(request.session.session_key, offices_for_booking)
            available_office = cache.get(request.session.session_key)
        return render(request, 'selection/floors.html', {
            'floors': Floor.objects.filter(id__in=list(Zone.objects.filter(id__in=
                                                         list(available_office.values_list('zone_id', flat=True)
                                                               .distinct())).values_list('floor', flat=True))),
        })
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
    bookings = Reservation.objects.filter(start_date__gte=datetime.strftime(datetime.now(), '%Y-%m-%d'), user=request.user)
    return render(request, 'offices/bookings.html',
                  {'user_bookings': bookings})


def cancel_booking(request, id):
    try:
        Reservation.objects.filter(id=id).delete()
        return redirect('/')
    except Exception as ex:
        return HttpResponse(status=400)
