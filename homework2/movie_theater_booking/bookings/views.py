from django.shortcuts import render

from rest_framework import viewsets

from .models import Movie, Seat, Booking

#from movie_theater_booking.bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.

#Movie View
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-date_joined')
    serializer_class = MovieSerializer

#Seat View
class SeatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seats to be viewed or edited.
    """
    queryset = Seat.objects.all().order_by('-date_joined')
    serializer_class = SeatSerializer

#Booking View
class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Booking.objects.all().order_by('-date_joined')
    serializer_class = BookingSerializer