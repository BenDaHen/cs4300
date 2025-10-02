from django.db import models

# Create your models here.

#Models will act as backend database to store the information for each entry

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
    seat_number = models.CharField(max_length=3, unique=True)

    #Booking Status
    booking_status = models.BooleanField(default=False) 

    #Print out Seat information
    def __str__(self):
        return f'''Seat Number: ({self.seat_number})\n
        Booking Status: ({self.booking_status})'''

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

    #Print out Booking information
    def __str__(self):
        return f'''Movie: ({self.movie})\n
        Seat: ({self.seat})\n
        User: ({self.user})\n
        Booking Date: ({self.booking_date})'''