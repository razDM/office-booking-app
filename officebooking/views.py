from django.shortcuts import render
from django.core.cache import cache


def homepage_view(request):
    cache.clear()
    return render(request, 'homepage.html',  {
        'title': 'Office Booking'})
