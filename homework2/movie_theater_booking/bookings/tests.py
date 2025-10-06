from django.test import TestCase
from django.utils import timezone
from .models import Movie, Seat, Booking
from datetime import date, timedelta

# Create your tests here.

#Movie Tests
class MovieModelTest(TestCase):
    """Tests for the Movie model"""

    #Sets up a test movie to be the same for all tests
    def setUp(self):
        self.movie = Movie.objects.create(
            movie_title = "Test Movie Title",
            movie_description = "This is a test movie",
            movie_release_date = date(2025, 1, 11),
            movie_duration=timedelta(hours=2, minutes=30)
        )

    #Test that a movie is correctly created
    def test_movie_creation(self):
        self.assertEqual(self.movie.movie_title, "Test Movie Title")
        self.assertEqual(self.movie.movie_description, "This is a test movie")
        self.assertEqual(self.movie.movie_release_date, date(2025, 1, 11))
        self.assertEqual(self.movie.movie_duration, timedelta(hours=2, minutes=30))
        self.assertEqual(Movie.objects.count(), 1)


    #Test that a movie is correctly updated
    def test_movie_update(self):
        self.movie.movie_title = "New Title"
        self.movie.movie_description = "New Description"
        self.movie.movie_release_date = date(2025, 2, 22)
        self.movie.movie_duration = timedelta(hours=1, minutes=20)
        self.movie.save()

        self.assertEqual(self.movie.movie_title, "New Title")
        self.assertEqual(self.movie.movie_description, "New Description")
        self.assertEqual(self.movie.movie_release_date, date(2025, 2, 22))
        self.assertEqual(self.movie.movie_duration, timedelta(hours=1, minutes=20))

    #Test that a movie is correctly deleted
    def test_movie_delete(self):
        self.movie.delete()

        self.assertEqual(Movie.objects.count(), 0)

#Seat Tests
class SeatModelTest(TestCase):
    """Tests for the seat model"""

    #Sets up a test seat to be the same for all tests
    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number = 10,
            booking_status = True
        )

    #Test that a seat is correctly created
    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, 10)
        self.assertEqual(self.seat.booking_status, True)
        self.assertEqual(Seat.objects.count(), 1)

    #Test that a seat is correctly edited
    def test_seat_edit(self):
        self.seat.seat_number = 20
        self.seat.booking_status = False
        self.seat.save()

        self.assertEqual(self.seat.seat_number, 20)
        self.assertEqual(self.seat.booking_status, False)

    #Test that a seat is correctly deleted
    def test_seat_delete(self):
        self.seat.delete()

        self.assertEqual(Seat.objects.count(), 0)

#Booking Model
class BookingModelTest(TestCase):
    """Tests for the booking model"""

    #Sets up a booking to be the same for all tests
    def setUp(self):
         #Set up a Movie and Seat to be used with the booking
        self.movie = Movie.objects.create(
            movie_title = "Test Movie Title",
            movie_description = "This is a test movie",
            movie_release_date = date(2025, 1, 11),
            movie_duration=timedelta(hours=2, minutes=30)
        )

        self.seat = Seat.objects.create(
            seat_number = 10,
            booking_status = True
        )

        #Create the booking using the movie and seat
        self.booking = Booking.objects.create(
            booked_movie = self.movie,
            seat = self.seat,
            booked_date = date(2025, 5, 25),
            booked_user = "User"
        )

        self.movie2 = Movie.objects.create(
            movie_title = "Test Movie Title 2",
            movie_description = "This is a test movie 2",
            movie_release_date = date(2025, 3, 29),
            movie_duration=timedelta(hours=1, minutes=30)
        )

        self.seat2 = Seat.objects.create(
            seat_number = 20,
            booking_status = False
        )

        #Set up an additional movie and seat for editing


    #Test that a booking is correctly created
    def test_booking_creation(self):
        self.assertEqual(self.booking.booked_movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.booked_date, date(2025, 5, 25))
        self.assertEqual(self.booking.booked_user, "User")
        self.assertEqual(Booking.objects.count(), 1)

    #Test that a booking is correctly edited
    def test_booking_edit(self):
        self.booking.booked_movie = self.movie2
        self.booking.seat = self.seat2
        self.booking.booked_date = date(2025, 4, 24)
        self.booking.booked_user = "User 2"
        self.booking.save()

        self.assertEqual(self.booking.booked_movie, self.movie2)
        self.assertEqual(self.booking.seat, self.seat2)
        self.assertEqual(self.booking.booked_date, date(2025, 4, 24))
        self.assertEqual(self.booking.booked_user, "User 2")

    #Test that a booking is correctly deleted
    def test_booking_delete(self):
        self.booking.delete()

        self.assertEqual(Booking.objects.count(), 0)