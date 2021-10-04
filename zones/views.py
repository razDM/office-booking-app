from django.shortcuts import render
from zones.models import Zone


def show_zones(request):
    return render(request, 'zones/zones.html', {
        'zones': Zone.objects.all(),
    })
