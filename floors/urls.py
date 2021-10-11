from django.urls import path
from floors.views import show_floors,show_floors_details

app_name = 'floors'

urlpatterns = [
    path('', show_floors, name='all'),
    path('<int:id>/', show_floors_details, name='details'),

]
