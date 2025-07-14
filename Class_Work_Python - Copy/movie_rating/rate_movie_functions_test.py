import unittest

from movie_rating.rating_movie_function import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.movies = MovieList()

    def test_movies_is_added(self):
        title, timestamp = self.movies.add_movie("King of Boys")
        self.assertIn("King of Boys", self.movies.movies)
        self.assertIsInstance(timestamp, str)

    def test_movie_not_added(self):
        result = self.movies.rate_movie("Dumebi goes to school", 4)
        self.assertEqual(result, ("movie not found", "Dumebi goes to school"))


    def test_movie_rating(self):
            self.movies.add_movie("Twist of fate")
            expected = self.movies.rate_movie("Twist of fate", 4)
            self.assertEqual(expected, ("Twist of fate", 4))
            self.assertEqual(self.movies.rate_movie("Twist of fate", 4), expected)

    def test_movie_rating_error(self):
        self.movies.add_movie("Jagun Jagun")
        result = self.movies.rate_movie("Jagun Jagun", 6)
        self.assertEqual(result, ("rate must be between 1 and 5", 6))

    def test_movie_rating_less_than_1(self):
        self.movies.add_movie("Buka Street")
        expected = self.movies.rate_movie("Buka Street", 0)
        self.assertEqual(expected, ("rate must be between 1 and 5", 0))

    def test_average_rating_for_multiples(self):
        self.movies.add_movie("Buka Street")
        self.movies.rate_movie("Buka Street", 5)
        self.movies.rate_movie("Buka Street", 5)
        average = self.movies.average_rating("Buka Street")
        self.assertEqual(average, 5.0)

    def test_average_rating_for_single(self):
        self.movies.add_movie("Buka Street")
        self.movies.rate_movie("Buka Street", 4)
        average = self.movies.average_rating("Buka Street")
        self.assertEqual(average, 4.0)

    def test_average_rating_return_zero_for_unrated_movie(self):
        self.movies.add_movie("Inception")
        self.assertEqual(self.movies.average_rating("Inception"), 0.0)


if __name__ == '__main__':
    unittest.main()

