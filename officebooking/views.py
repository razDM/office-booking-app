from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html',  {
        'title': 'Office Booking',
        'services': [{
            'name': 'Available Floors',
            'value': '2',
        }, {
            'name': 'Available Zones',
            'value': '8'
        }, {
            'name': 'Available Seats',
            'value': '32'
        }]
    })
