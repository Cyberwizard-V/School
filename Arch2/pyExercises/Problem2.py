"""
In a particular jurisdiction, taxi fares consist of a base fare of 4.00 eur, plus 0.25 eur for every 140 meters traveled.
Write a function called "calculate_fare"that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only result. 
Write a main program that interacts with the user and calls the function to produce and print the final result.
"""

def calculate_fare(distance):
        varMeter = distance * 1000
        if varMeter % 140 == 0:
            meterDiv = varMeter // 140
            cost = 4 + (meterDiv * 0.25)
            return(cost)
        else:
            meterDiv = varMeter // 140
            cost = 4 + 0.25 + (meterDiv * 0.25)
            return(cost)

def main():
    distance = float(input("Enter the distance traveled in kilometers: "))
    print("The total fare is", calculate_fare(distance), "eur")

if __name__ == "__main__":
    main()
    