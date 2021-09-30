from django.urls import path
from zones.views import show_zones

app_name = 'zones'

urlpatterns = [
    path('', show_zones, name='all'),
]
