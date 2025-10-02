#Routing URLS

from django.urls import path, include
from rest_framework import routers
from . import views

#Add Routers
router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

#URL Patterns

#Add API pattern
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]