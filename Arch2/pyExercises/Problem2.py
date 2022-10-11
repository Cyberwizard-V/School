def calculate_fare(distance=0):
    varMeter = distance * 1000
    if varMeter % 140 == 0:
        meterDiv = varMeter // 140
        cost = 4 + (meterDiv * 0.25)
        return(cost)
    else:
        meterDiv = varMeter // 140
        cost = 4 + 0.25 + (meterDiv * 0.25)
        return(cost)


if __name__ == "__main__":
    distance = float(input("Enter the distance traveled in kilometers: "))
    print("The total fare is", calculate_fare(distance), "eur")
    calculate_fare(distance)