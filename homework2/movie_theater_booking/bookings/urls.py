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
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]