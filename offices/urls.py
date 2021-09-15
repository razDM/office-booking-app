from django.urls import path
from offices.views import show_all_offices, show_offices_details

app_name = 'offices'

urlpatterns = [
    path('', show_all_offices, name='all'),
    path('<int:offices_id>/', show_offices_details, name='details'),

]
