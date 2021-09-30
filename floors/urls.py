from django.urls import path
from floors.views import show_floors

app_name = 'floors'

urlpatterns = [
    path('', show_floors, name='all'),
]
