from django.shortcuts import render
from offices.models import Office


offices = [{
    'id': 1,
    'floor': 1,
    'name': 'Office #1'
}, {
    'id': 2,
    'floor': 2,
    'name': 'Office #2'
}, {
    'id': 3,
    'floor': 3,
    'name': 'Office #3'

}]


def show_all_offices(request):
    offices = Office.objects.all()

    return render(request, 'offices/offices.html', {
        'offices': offices,
    })

def show_offices_details(request, offices_id):
    founded_offices = [p for p in offices if p['id'] == offices_id]

    if len(founded_offices) == 0:
        raise Http404(f'Office Id = {offices_id}, does not exist')

    return render(request, 'offices/details.html', {
        'offices': founded_offices[0]
    })
