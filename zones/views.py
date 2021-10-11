from django.shortcuts import render, get_object_or_404
from zones.models import Zone
from offices.models import Office


def show_zones(request):
    return render(request, 'zones/zones.html', {
        'zones': Zone.objects.all(),
    })


def show_zones_details(request, zones_id):
    office = get_object_or_404(Office, pk=zones_id)
    return render(request, 'offices/details.html', {
        'office': office,
    })

