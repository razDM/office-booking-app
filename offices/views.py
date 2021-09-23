from django.shortcuts import render, get_object_or_404
from offices.models import Office


def show_all_offices(request):
    offices = Office.objects.all()

    return render(request, 'offices/offices.html', {
        'offices': offices,
    })


def show_offices_details(request, offices_id):
    office = get_object_or_404(Office, pk=offices_id)
    return render(request, 'offices/details.html', {
        'office': office,
    })

