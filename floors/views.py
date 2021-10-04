from django.shortcuts import render
from floors.models import Floor


def show_floors(request):
    return render(request, 'floors/floors.html', {
        'floors': Floor.objects.all(),
    })
