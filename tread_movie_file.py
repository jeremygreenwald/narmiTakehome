import unittest

import datetime

from schedule import read_movie_file


class MyTestCase(unittest.TestCase):
    def test_something(self):
        movies = read_movie_file("test_input.txt")
        self.assertEqual(movies[0]["Movie Title"], "There's Something About Mary")  # add assertion here
        self.assertEqual(movies[0][" Release Year"], 1998)
        self.assertEqual(movies[0][" MPAA Rating"], 'R')
        self.assertEqual(movies[0][" Run Time"], datetime.time(hour=2, minute=14))


if __name__ == '__main__':
    unittest.main()
