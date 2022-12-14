'''
Implement a program that using the data from movies.json, shows the following information:

    The number of movies released in 2004.
    The number of movies in which the genre is Science Fiction.
    All movies with actor Keanu Reeves.
    All movies with actor Sylvester Stallone released between 1995 and 2005.

Using data from movies.json, make the following adjustments and write it back to the file:

    Change the release year from the movie Gladiator from 2000 to 2001.
    Set the release year from the oldest movie to one year earlier.
    Actor Natalie Portman changed her name to Nat Portman. Adjust this at all movies she is in.
    Actor Kevin Spacey got cancelled. Remove his name from all movies he is in.

Using data from movies.json, implement a program that allows the following: Create a menu with the input options shown below:
[I] Show all information about the movies found in a user friendly format. If there are multiple movies by the same name, show these with the release year to user and let them pick which movie they meant.
[M] Make modification based on assignment
[S] Searching a title should not be case sensitive.
[C] Extend your program by allowing the user to change the title and/or release year of the selected movie (after searching it). Implement this in a user friendly way.
[Q] Quit Program
'''
import os
import sys
import json


with open('movies.json', 'r+', encoding='utf-8') as json_file:
    data = json.load(json_file)
    json_file.close()


def get_movies_with_actor_from_to(
        beginYear: int,
        endYear: int,
        actor: str) -> list:
    moviesButInOneLine = [
        x["title"] for x in data if actor in x["cast"] and beginYear <= x["year"] <= endYear]
    return moviesButInOneLine


def get_moviescount_from_year(year: int) -> int:
    count = 0
    for x in data:
        if x['year'] == year:
            count += 1

    return count


def get_moviescount_from_genre(genre: int) -> int:
    count = 0
    for x in data:
        if genre in x['genres']:
            count += 1
    return count


def get_movies_from_actor(actor: str) -> list:
    movies = [x['title'] for x in data if actor in x['cast']]
    return movies


def change_year_from_movie(
        movieName: str,
        selectYear: int,
        changeYear: int) -> None:
    for x in data:
        if x['title'] == movieName and x['year'] == selectYear:
            x['year'] = changeYear
    jsonFile = open("movies.json", "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()


def change_actorname_from_movie(selectActor: str, changeName: str) -> None:
    for x in data:
        if selectActor in x['cast']:
            index = x['cast'].index(selectActor)
            x['cast'][index] = changeName


def delete_actor_from_movie(selectActor: str) -> None:
    for x in data:
        if selectActor in x['cast']:
            x['cast'].remove(selectActor)

    jsonFile = open("movies.json", "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()
    print('changed?')


def get_movie_from_title(movie: str) -> list:
    movies = [x["title"] for x in data if movie in x["title"]]
    return movies


def change_year_from_movie_and_name(
        movieName: str,
        selectYear: int,
        changeYear: int,
        newTitle: str) -> None:
    for x in data:
        if x['title'] == movieName and x['year'] == selectYear:
            x['year'] = changeYear
            x['title'] = newTitle
    jsonFile = open("movies.json", "w+")
    jsonFile.write(json.dumps(data, indent=4))
    jsonFile.close()

# We created the menu layout for you
# Only given imports are allowed


def main() -> None:
    while True:
        print("[I] Movie information overview")
        print("[M] Make modification based on assignment")
        print("[S] Search a movie title ")
        print("[C] Change title and/or release year by search on title")
        print("[Q] Quit program")
        getInput = input()
        if getInput == "I":
            print(get_moviescount_from_year(2004))
            print(get_moviescount_from_genre("Science Fiction"))
            print(get_movies_from_actor('Keanu Reeves'))
            print(
                get_movies_with_actor_from_to(
                    1995,
                    2005,
                    "Sylvester Stallone"))
            print(
                change_actorname_from_movie(
                    'Natalie Portman',
                    'Nat Portman'))
            print(delete_actor_from_movie('Kevin Spacey'))
            change_year_from_movie_and_name(
                "Rambo", 2008, 2022, "Rambo Remastered")
        elif getInput == "M":
            print(change_year_from_movie('Gladiator', 2000, 2001))
            print(
                change_year_from_movie(
                    'After Dark in Central Park',
                    1900,
                    1899))
        elif getInput == "S":
            x = input('Search a movie: ')
            print(get_movie_from_title(x))
        elif getInput == "C":
            print(change_year_from_movie('Gladiator', 2000, 2001))
        elif getInput == "Q":
            quit()

    # Implement rest of functionality


if __name__ == "__main__":
    main()
