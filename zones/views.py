from django.shortcuts import render, get_object_or_404
from zones.models import Zone
from offices.models import Office


def show_zones(request):
    return render(request, 'zones/zones.html', {
        'zones': Zone.objects.all(),
    })


def show_zones_details_by_floor(request, floor_id):
    # zone = get_object_or_404(Zone, floor_id=floor_id)
    return render(request, 'zones/zones.html', {
        'zones': Zone.objects.filter(floor_id=floor_id),
    })

