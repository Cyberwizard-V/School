class Customer:

    def __init__(abc, name):
        abc.name = name

    def print(abc):
        return abc.name


class Car:
    sold = False
    sold_to = "-"

    def __init__(abc, brand: str, model: str, color: str, price: int):
        abc.brand = brand
        abc.model = model
        abc.color = color
        abc.price = price

    def sell(abc, name):
        abc.sold = True
        abc.sold_to = name
        return abc.sold

    def print(abc):
        print(f"""Brand: {abc.brand}, Model: {abc.model}, Color: {abc.color}, Price: {abc.price}, Sold-Status: {abc.sold}, Sold-To: {abc.sold_to} """)


class Motorcycle:
    sold = False
    sold_to = "-"

    def __init__(abc, brand: str, model: str, color: str, price: int):
        abc.brand = brand
        abc.model = model
        abc.color = color
        abc.price = price

    def sell(abc, name):
        abc.sold = True
        abc.sold_to = name
        return abc.sold

    def print(abc):
        print(f"""Brand: {abc.brand}, Model: {abc.model}, Color: {abc.color}, Price: {abc.price}, Sold-Status: {abc.sold}, Sold-To: {abc.sold_to} """)


# Create cars
Car1 = Car("SEAT", "Ibiza", "Yellow", 3500)
Car2 = Car("Nissan", "Skyline", "Purple", 32000)
Car3 = Car("Mazda", "Rx7", "Blue", 12000)

# Create a Customer
Customer1 = Customer("John")

Car2.print()
if Car3.sell(Customer1.print()):
    Car3.print()
    print("Car has been sold")


def main():
    print("I love cars")


if __name__ == "__main__":
    main()
