from django.urls import path
from selection.views import show_floors,show_floors_details, show_all_offices, show_offices_details, show_zones, show_zones_details_by_floor

app_name = 'selection'

urlpatterns = [
    path('floors', show_floors, name='all_floors'),
    path('floors/<int:id>/', show_floors_details, name='floor_details'),
    path('offices', show_all_offices, name='all_offices'),
    path('offices/<int:zone_id>/', show_offices_details, name='office_details'),
    path('zones', show_zones, name='all_zones'),
    path('zones/<int:floor_id>/', show_zones_details_by_floor, name='zones_by_floor'),
]
