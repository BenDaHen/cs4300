from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework import viewsets

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

import datetime

# Create your views here.

#The views showcase each serializer, and through the serializers
#are able to show the model data

# Template Views
def home(request):
    """Home page view"""
    return render(request, 'bookings/base.html')

def movie_list_template(request):
    """Display all movies in a template"""
    movies = Movie.objects.all().order_by('-movie_release_date')
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def booking_list_template(request):
    """Display all bookings in a template"""
    bookings = Booking.objects.all().order_by('-booked_date')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def seat_booking_view(request, movie_id):
    """Display available seats for a specific movie"""
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('seat_number')
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

def confirm_booking_view(request, movie_id, seat_id):
    """Confirm and create a booking"""
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)
    
    # Check if seat is already booked
    if seat.booking_status:
        messages.error(request, f'Seat {seat.seat_number} is already booked!')
        return redirect('seat-booking', movie_id=movie_id)
    
    # Create the booking
    booking = Booking.objects.create(
        booked_movie=movie,
        seat=seat,
        booked_date = datetime.date.today(),
        booked_user=request.user.username if request.user.is_authenticated else 'Guest'
    )
    
    # Update seat status
    seat.booking_status = True
    seat.save()
    
    messages.success(request, f'Successfully booked Seat {seat.seat_number} for {movie.movie_title}!')
    return redirect('booking-list')

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
    queryset = Booking.objects.all().order_by('-booked_movie')
    serializer_class = BookingSerializer