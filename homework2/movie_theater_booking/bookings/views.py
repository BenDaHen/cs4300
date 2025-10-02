from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

def index(request):
    return HttpResponse("Booking Page")


# Create your views here.

#The views showcase each serializer, and through the serializers
#are able to show the model data

#Movie View
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-movie_release_date')
    serializer_class = MovieSerializer
    

#Seat View
class SeatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seats to be viewed or edited.
    """
    queryset = Seat.objects.all().order_by('-seat_number')
    serializer_class = SeatSerializer

#Booking View
class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Booking.objects.all().order_by('-booking_date')
    serializer_class = BookingSerializer