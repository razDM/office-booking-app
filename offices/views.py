from django.shortcuts import render
from .forms import AvailabilityForm
from django.http import HttpResponse
from django.db import IntegrityError
from offices.models import Reservation
from offices.booking_functions.availability import check_availability
from selection.models import Office, Zone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import redirect



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
                   'start_date': request.GET['start_date'], 'end_date': request.GET['end_date']})


def book_now(request, id, start_date, end_date):
    office_details = Office.objects.get(id=id)
    zone_details = Zone.objects.get(id=office_details.zone_id)
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
