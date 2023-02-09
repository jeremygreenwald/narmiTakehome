
from csv import DictReader


def display_schedule(input_file):
    schedule = create_schedule(input_file)
    print_schedule(schedule)

def print_schedule(schedule):
    print(schedule)


def create_schedule(input_file):
    movies = read_movie_file(input_file)
    return []

def read_movie_file(input_file):
    with open(input_file) as f:
        dict_reader = DictReader(f)
        list_of_movies = list(dict_reader)
        print(list_of_movies)

    return list_of_movies
