from django.db import models

# Create your models here.

#Movie: title, description, release date, duration
class Movie(models.Model):
    #Title
    movie_title = models.CharField(max_length=50)

    #Description
    movie_description = models.CharField(max_length=500)

    #Release Date
    movie_release_date = models.DateTimeField("date published")

    #Duration
    movie_duration = models.CharField(max_length=5)


#Seat: seat number, booking status
class Seat(models.Model):
    #Seat Number
    seat_number = models.CharField(max_length=3)

    #Booking Status
    booking_status = models.CharField(max_length=10)

#Booking: movie, seat, user, booking date
class Booking(models.Model):
    #Movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    #Seat
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    #User
    user = models.CharField(max_length=50)

    #Booking Date
    booking_date = models.DateTimeField("date booked")