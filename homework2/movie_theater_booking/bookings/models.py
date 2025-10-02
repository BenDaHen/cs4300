from django.db import models

# Create your models here.

#Models will act as backend database to store the information for each entry

#By running makemigrations and migrate, the database will be saved

#Movie: title, description, release date, duration
class Movie(models.Model):
    objects = models.Manager

    #Title
    movie_title = models.CharField(max_length=50)

    #Description
    movie_description = models.TextField()

    #Release Date
    movie_release_date = models.DateField()

    #Duration
    movie_duration = models.DurationField()

    #Print out Movie information
    def __str__(self):
        return f'''Title: ({self.movie_title})\n
        Description: ({self.movie_description})\n
        Release Date: ({self.movie_release_date})\n
        Duration: ({self.movie_duration})'''


#Seat: seat number, booking status
class Seat(models.Model):
    #Seat Number
    seat_number = models.IntegerField(unique=True)

    #Booking Status
    booking_status = models.BooleanField(default=False)

    #Print out Seat information
    def __str__(self):
        return f'''Seat Number: ({self.seat_number})\n
        Booking Status: ({self.booking_status})'''

#Booking: movie, seat, user, booking date
class Booking(models.Model):
    #Book for which movie
    booked_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)

    #Seat
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, unique=True)

    #Pick the date to book for
    booked_date = models.DateField(null=True, blank=True)

    #Who the seat is booked by
    booked_user = models.CharField(max_length=20, null=True, blank=True)

    #Print out Booking information
    def __str__(self):
        return f'''Movie: ({self.booked_movie})\n
        Seat: ({self.seat})\n
        Date: ({self.booked_date})\n
        User: ({self.booked_user})'''