import os
import sys
import csv
import pprint

'''
Implement a program that shows the following information:

    How many games got banned in Israel?
    Which country got the most games banned?
    How many games within the Assasins Creed series are currently banned? Don't count duplicates banned in different countries.
    Show all games (and the details) banned in Germany.
    Show all countries (and the details) the game Red Dead Redemption got banned in.

Implement a program that makes the following adjustments and write it back to the file:

    Germany got a new law that accepts all games as a form of art. Remove all records with Germany from the file.
    The game Silent Hill VI got renamed to Silent Hill Remastered, rename this in all corresponding records.
    The ban on the game Bully in Brazil has been lifted. Change the status to Ban Lifted.
    The game Manhunt II is by several countries. It is incorrectly listed as genre Stealth, change the genre to Action in all corresponding records.

Using data from bannedvideogames.csv, implement a program that allows the following: Create a menu with the input options shown below:
[I] Print request info from assignment
[M] Make modification based on assignment
[A] Add game > ask the user to insert all needed information and write it to the file.
You can use the following list for keys: python ['id', 'name', 'series', 'country', 'details', 'category', 'status', 'wikipedia', 'image', 'summmary', 'developer', 'publisher', 'genre', 'homepage']
[O] Overview of banned games per country python <country_name> - <amount_banned> - <game_name_1> - <game_name_2> ...
[S] Search the dataset by country. Show name and details from banned video games in that country.

<game_name_1> - <game_details_1>
<game_name_2> - <game_details_2>
...


[Q] Quit program

'''
def get_banned_count_from_country(CountryName : str ) -> int:
    count = 0
    with open("bannedvideogames.csv", 'r', encoding="utf-8") as file:
        csvreader = csv.DictReader(file)
        for i in csvreader:
            if CountryName in i['Country']:
                count += 1
    return count

def get_most_banned() -> int:
    with open("bannedvideogames.csv", 'r', encoding="utf-8") as file:
        csvreader = csv.DictReader(file)
        Countries = []
        for i in csvreader:
            Countries.append(i['Country'])

    return "Most banned: ", max(set(Countries), key=Countries.count)

# How many games within the Assasins Creed series are currently banned? Don't count duplicates banned in different countries.
def get_videogame_banned_count(gameName : str):
    count = 0
    with open("bannedvideogames.csv", 'r', encoding="utf-8") as file:
        csvreader = csv.DictReader(file)
        for i in csvreader:
            if gameName in i['Series']:
                count += 1
    return count
    
    
# Show all games (and the details) banned in Germany.
def get_banned_details_from_country(countryName : str) -> None:
    with open("bannedvideogames.csv", 'r', encoding="utf-8") as file:
        csvreader = csv.DictReader(file)
        for i in csvreader:
            if i['Country'] == countryName:
                print(i['Details'])
                print(i['Game'])

# Show all countries (and the details) the game Red Dead Redemption got banned in.
def get_banned_countries_where(GameName : str) -> None:
    with open("bannedvideogames.csv", 'r', encoding="utf-8") as file:
        csvreader = csv.DictReader(file)
        for i in csvreader:
            if i['Game'] == GameName:
                print(i['Country'])

def remove_rows_country(Country) -> None:
    myList = list()
    with open("bannedvideogames.csv", 'r', encoding="utf-8") as file:
        csvreader = csv.DictReader(file)
        for i in csvreader:
            myList.append(i)
            if i['Country'] == Country:
                 myList.remove(i)
    with open('bannedvideogames2.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(myList)


# We created the menu layout for you
# Only given imports are allowed
def main(filename: str) -> None:
    pass
    # print("[I] Print request info from assignment")
    #print(get_most_banned())
    #print(get_banned_count_from_country("Australia"))
    #print(get_videogame_banned_count("Assassin's Creed"))
    #get_banned_details_from_country('Germany')
    #get_banned_countries_where('Red Dead Redemption')

    # print("[M] Make modification based on assignment")
    # print("[A] Add new game to list")
    # print("[O] Overview of banned games per country")
    # print("[S] Search the dataset by country")
    # print("[Q] Quit program")

    # Implement rest of functionality

if __name__ == "__main__":
    remove_rows_country("Germany")