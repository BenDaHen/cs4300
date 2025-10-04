#Routing URLS

from django.urls import path, include
from rest_framework import routers
from . import views

#Add Routers
#Routers will take the url pattern defined below
#And will register a new route on top of it to display the associated viewset
router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

#URL Patterns
#These determine what is visible at each URL path
urlpatterns = [
    #Template URLS
    path('', views.home, name='home'),
    path('movies/', views.movie_list_template, name='movies'),
    path('bookings/', views.booking_list_template, name='bookings'),
    path('book-seat/<int:movie_id>/', views.seat_booking_view, name='book-seat'),
    path('confirm-booking/<int:movie_id>/<int:seat_id>/', views.confirm_booking_view, name='confirm-booking'),
    #API Endpoints
    path('api/', include(router.urls)),
]