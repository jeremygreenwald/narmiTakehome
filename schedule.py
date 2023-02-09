import datetime
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
        for movie in list_of_movies:
            movie[" Release Year"] = int(movie[" Release Year"])
            movie[" MPAA Rating"] = movie[" MPAA Rating"].strip(" ")
            runtime = movie[" Run Time"].strip(" ")
            movie[" Run Time"] = datetime.time(hour=int(runtime.split(':')[0]),
                                               minute=int(runtime.split(':')[1]))
    return list_of_movies
