import datetime
from csv import DictReader


def read_movie_list(file_name):
    with open(file_name, 'r') as file:
        csv_file = DictReader(file)
        data = [dict(d) for d in csv_file]

        for movie in data:
            movie[' Release Year'] = int(movie[' Release Year'])
            movie[' MPAA Rating'] = movie[' MPAA Rating'].strip(" ")
            run_time = movie[' Run Time'].strip(" ")
            movie[' Run Time'] = int(run_time.split(":")[0]) * 60 + \
                                 int(run_time.split(":")[1])
    return data

def create_schelude(movies, day):
    last_movie_end = theater_close_time("Monday")
    first_movie_start = theater_movie_start("Monday")

    curr = last_movie_end
    showtimes = []
    for movie in movies:
        while curr - movie[" Run Time"] > first_movie_start:
            start_time = curr - movie[" Run Time"]
            start_time = start_time - (start_time % 5)
            showtimes.append( (start_time, curr) )

            curr = start_time - 35

    showtimes.reverse()
    print(showtimes)
    return showtimes


def theater_close_time(day):
    return 23 * 60 - 1


def theater_movie_start(day):
    return 8 * 60 + 60 + 35
