from django.urls import path
from offices.views import get_available_offices, book_now, do_booking, back_button, my_bookings,cancel_booking


app_name = 'offices'

urlpatterns = [
    path('', get_available_offices, name='ReservationFormView'),
    path('reserveNow/<int:id>/<str:start_date>/<str:end_date>/', book_now, name="book_now"),
    path('doBooking/<int:id>/<str:start_date>/<str:end_date>/', do_booking, name="do_booking"),
    path('backToHome/', back_button, name="back_to_homepage"),
    path('myBookings/', my_bookings, name='my_bookings'),
    path('cancelBooking/<int:id>/',cancel_booking, name='cancel_booking')

]
