#Serializers

#Imports
from rest_framework import serializers
from .models import Movie, Seat, Booking

#Movie Serializer
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release date', 'duration']

#Seat Serializer
class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat number', 'booking status']

#Booking Serializer
class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'booking date']

