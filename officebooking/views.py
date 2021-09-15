from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html',  {
        'title': 'Django Office booking',
        'services': [{
            'name': 'Available offices',
            'value': '5',
        }, {
            'name': 'Employees booked an office: ',
            'value': '15'
        }]
    })
