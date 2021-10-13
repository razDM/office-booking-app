from django.shortcuts import render, get_object_or_404
from floors.models import Floor
from zones.models import Zone


def show_floors(request):
    return render(request, 'floors/floors.html', {
        'floors': Floor.objects.all(),
    })


def show_floors_details(request, floors_id):
    zone = get_object_or_404(Zone, pk=floors_id)
    return render(request, 'zones/zones.html', {
        'zones': zone,
    })
