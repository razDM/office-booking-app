from django.shortcuts import render
from offices.models import Zone


def show_zones(request):
    return render(request, 'zones/zones.html', {
        'zone': Zone.objects.all(),
    })
