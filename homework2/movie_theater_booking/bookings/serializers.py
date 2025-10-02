#Serializers

#Imports
from rest_framework import serializers
from .models import Movie, Seat, Booking

#Movie Serializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_title', 'movie_description', 'movie_release_date', 'movie_duration']

#Seat Serializer
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_number', 'booking_status']

#Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'booking_date']

