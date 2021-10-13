from django.urls import path
from zones.views import show_zones,show_zones_details_by_floor

app_name = 'zones'

urlpatterns = [
    path('', show_zones, name='all'),
    path('<int:floor_id>/', show_zones_details_by_floor, name='floor_zones'),

]
