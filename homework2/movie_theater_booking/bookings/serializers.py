#Serializers

#Imports
from rest_framework import serializers
from .models import Movie, Seat, Booking

#The serializers allow the models to be edited through the 
#server itself rather than just in the shell

#Movie Serializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_title', 'movie_description', 'movie_release_date', 'movie_duration']

#Seat Serializer
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'booking_status']

#Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'booked_movie', 'seat', 'booked_date', 'booked_user']

