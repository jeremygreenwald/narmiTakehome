import unittest
import datetime

from schedule import read_movie_list, create_schelude


class MyTestCase(unittest.TestCase):
    def test_something(self):
        movies = read_movie_list("test_input.txt")
        self.assertEqual(movies[0]["Movie Title"], "There's Something About Mary")
        self.assertEqual(movies[0][" Release Year"], 1998)
        self.assertEqual(movies[0][" MPAA Rating"], "R")
        self.assertEqual(movies[0][" Run Time"], 2 * 60 + 14)

    def test_schedule(self):
        test_movies = [ {"Movie Title": "There's Something About Mary",
           " Release Year": 1998,
           " MPAA Rating": "R",
           " Run Time": 2*60+14} ]
        sch = create_schelude(test_movies, "Monday")
        self.assertEqual(sch[-1], (1245, 1379))
        self.assertEqual(sch[0], (735, 869))

if __name__ == '__main__':
    unittest.main()
