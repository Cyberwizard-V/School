'''
The following data reprsents average tempratures of the third month for 1995, 2010, and 2020 recorded in Amsterdam.
Implement a program that given this data prints the answers for the following questions (each seperate line):
	- How many unique days have equal average tempratues in March 1995 and March 2010.
	- How many unique days have equal average tempratues in March 1995 and March 2020. 
	- Which year has a day with highest temprature in March?
	- Which year had the warmest March?
'''
temperatures = (
    ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5',
     '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
    ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7',
     '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
    ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9',
     '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
)
year1, month1, temp1 = temperatures[0]
year2, month2, temp2 = temperatures[1]
year3, month3, temp3 = temperatures[2]

def equal_temp(temp1, temp2):
    seen = set()
    bigList = temp1+temp2
    equalTemp = [x for x in bigList if x in seen or seen.add(x)]
    return len(equalTemp)

# def warmest_march():
#     warmest = 0
#     year1995 = sum(temp1)
#     year2010 = sum(temp2)
#     year2020 = sum(temp3)
#     if year1995 > year2010 and year1995 > year2020:
#         warmest = year1
#     elif year2010 > year1995 and year2010 > year2020:
#         warmest = year2
#     elif year2020 > year1995 and year2020 > year2010:
#         warmest = year3

#     return warmest


# def highest_tempMarch():
#     for year, month, temp in temperatures:
#         if max(temp) == warmest_march():
#             return year
            
if __name__ == "__main__":
    print(equal_temp(temp1, temp2))
    print(equal_temp(temp1, temp3))
    # print(highest_tempMarch())
    print()