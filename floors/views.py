from django.shortcuts import render
from models.floors import Floor


def show_floors(request):
    return render(request, 'floors/floors.html', {
        'floors': Floor.objects.all(),
    })
