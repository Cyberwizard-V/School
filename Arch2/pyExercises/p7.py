import os
import sys


def load_txt_file(file_name):

    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


dicted = {}
for x in load_txt_file("NLAMSTDM.txt"):
    year = int(x[2])
    month = int(x[0])
    temp = float(x[3])

    if year not in dicted:
        dicted[year] = {}

    if month not in dicted[year]:
        dicted[year][month] = []

    dicted[year][month].append(temp)


def average_temp_per_year(temperatures: dict):

    averageTemps = []
    for year, month in temperatures.items():
        totalTemp, totalDays = 0, 0
        for days in month.values():
            totalTemp += sum(days)
            totalDays += len(days)
        averageTemps.append((year, round(totalTemp / totalDays, 4)))
    return averageTemps


def average_temp_per_month(temperatures: dict):

    averageTempMonth = []
    for month, temps in temperatures.items():
        totalTemp, totalDays = 0, 0
        totalTemp += sum(temps)
        totalDays += len(temps)
        averageTempMonth.append((month, round(totalTemp / totalDays, 3)))
    return averageTempMonth


def fahrenheit_to_celsius(fahrenheit: float):

    return round((fahrenheit - 32) * (5 / 9), 4)


if __name__ == "__main__":
    selecter = input("")
    if selecter == "1":
        print(average_temp_per_year(dicted))
    elif selecter == "2":
        print(list(map(lambda data: (data[0], round(
            (data[1] - 32) * (5 / 9), 4)), average_temp_per_year(dicted))))
    elif selecter == "3":
        sorting = average_temp_per_year(dicted)
        sorting.sort(key=lambda a: a[1])
        print((sorting[-1][0], sorting[0][0]))
    elif selecter == "4":
        yearSelect = int(input("Enter a year: "))
        avgTemps = []
        list_of_months = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'}
        for months, temps in dicted[yearSelect].items():
            totalTemp, totalDays = 0, 0
            totalTemp += sum(temps)
            totalDays += len(temps)
            avgTemps.append((months, round(totalTemp / totalDays, 3)))
        avgTemps.sort(key=lambda a: a[1])
        monthNumber = str(avgTemps[-1][0])
        print(list_of_months[monthNumber])
    elif selecter == "5":
        yearSelect = int(input("Enter a year: "))
        avgTemps = []
        list_of_months = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'}
        for months, temps in dicted[yearSelect].items():
            totalTemp, totalDays = 0, 0
            totalTemp += sum(temps)
            totalDays += len(temps)
            avgTemps.append((months, round(totalTemp / totalDays, 3)))
        avgTemps.sort(key=lambda a: a[1])
        monthNumber = str(avgTemps[0][0])
        print(list_of_months[monthNumber])
    elif selecter == "6":
        years = []
        for year in dicted:
            yearData = [year, {}]
            for month in range(1, len(dicted[year]) + 1):
                yearData[1][month] = round(sum(
                    map(fahrenheit_to_celsius, dicted[year][month])) / len(dicted[year][month]), 4)
                years.append(tuple(yearData))
        print(years)
    else:
        print("Incorrect input")
