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