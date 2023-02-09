import unittest

from schedule import read_movie_file


class MyTestCase(unittest.TestCase):
    def test_something(self):
        movies = read_movie_file("test_input.txt")
        self.assertEqual(movies[0]["Movie Title"], "There's Something About Mary")  # add assertion here
        self.assertEqual(movies[0][" Release Year"], " 1998")
        self.assertEqual(movies[0][" MPAA Rating"], ' R')
        self.assertEqual(movies[0][" Run Time"], " 2:14")


if __name__ == '__main__':
    unittest.main()
