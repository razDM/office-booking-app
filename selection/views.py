from django.shortcuts import render, get_object_or_404
from selection.models import Floor
from selection.models import Zone
from selection.models import Office


def show_floors(request):
    return render(request, 'selection/floors.html', {
        'floors': Floor.objects.all(),
    })


def show_floors_details(request, floors_id):
    zone = get_object_or_404(Zone, pk=floors_id)
    return render(request, 'selection/zones.html', {
        'zones': zone,
    })


def show_all_offices(request):
    offices = Office.objects.all()

    return render(request, 'selection/offices.html', {
        'offices': offices,
    })


def show_offices_details(request, zone_id):
    return render(request, 'selection/offices.html', {
        'offices': Office.objects.filter(zone_id=zone_id),
    })


def show_zones(request):
    return render(request, 'selection/zones.html', {
        'zones': Zone.objects.all(),
    })


def show_zones_details_by_floor(request, floor_id):
    return render(request, 'selection/zones.html', {
        'zones': Zone.objects.filter(floor_id=floor_id),
    })
