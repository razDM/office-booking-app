from django.shortcuts import render, get_object_or_404
from selection.models import Floor
from selection.models import Zone
from selection.models import Office
from django.core.cache import cache


def show_floors(request):
    available_office = cache.get(request.session.session_key)

    if available_office:
        return render(request, 'selection/floors.html',
                      {'floors': Floor.objects.filter(id__in=list(Zone.objects.filter(id__in=list(available_office.values_list('zone_id', flat=True).distinct())).values_list('floor', flat=True)))})
    else:
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
    return render(request, 'selection/all_offices.html', {
        'offices': offices,
    })


def show_offices_details(request, zone_id):
    available_office = cache.get(request.session.session_key)
    if available_office:
        return render(request, 'selection/offices.html', {
            'offices': available_office.filter(zone_id=zone_id),
            'start_date': request.session['start_date'],
            'end_date': request.session['end_date']
        })
    return render(request, 'selection/offices.html', {
        'offices': Office.objects.filter(zone_id=zone_id),
        'start_date': '1990-01-01',
        'end_date': '1990-01-01'
    })


def show_zones(request):
    return render(request, 'selection/zones.html', {
        'zones': Zone.objects.all(),
    })


def show_zones_details_by_floor(request, floor_id):
    available_office = cache.get(request.session.session_key)
    if available_office:
        return render(request, 'selection/zones.html', {
            'zones': Zone.objects.filter(id__in=list(available_office.values_list('zone_id', flat=True).distinct()),
                                         floor_id=floor_id)
        })
    else:
        return render(request, 'selection/zones.html', {
            'zones': Zone.objects.filter(floor_id=floor_id),
        })
