#Serializers

#Imports
from rest_framework import serializers
from .models import Movie, Seat, Booking

#Movie Serializer
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_title', 'movie_description', 'movie_release date', 'movie_duration']

#Seat Serializer
class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat number', 'booking status']

#Booking Serializer
class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'booking_date']

