from datetime import datetime

class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in
        

class CarParkingMachine:
    capacity = 10
    hourly_rate = 2.50
    parked_cars = {}
    
    def __init__(self, capacity, hourly_rate):
        self.capacity = capacity
        self.hourly_rate = hourly_rate

    def check_in(self, license_plate , time = datetime.now()):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, time)
            return True
        else:
            return False

    def check_out(self, license_plate):
        if license_plate in self.parked_cars:
            return self.get_parking_fee(license_plate)
        else:
            return False
    
    def get_parking_fee(self, license_plate):
        if license_plate in self.parked_cars:
            time = self.parked_cars[license_plate].check_in
            time = datetime.now() - time
            hours = time.total_seconds() / 3600
            hours = round(hours)
            if hours > 24:
                hours = 24
            return hours * self.hourly_rate + self.hourly_rate
        else:
            return False
#[I] Check-in car by license plate
#output: License registered (only if checked-in)
#or: Capacity reached!
#[O] Check-out car by license plate
#output: Parking fee: {parking_fee} (2 decimals!) EUR (if license is found)
#or: License {license_plate} not found!
#[Q] Quit program

def main():
    x = CarParkingMachine(10, 2.50)
    while True:
        print("""
                [I] Check-in car by license plate
                [O] Check-out car by license plate
                [Q] Quit program
                """)
        choice = input("Choose an option: ").upper()
        if choice == "I":
            time = datetime.now()
            license_plate = input("License plate: ")
            if x.check_in(license_plate, time):
                print("License registered!")
            else:
                print("Capacity reached!")
        elif choice == "O":
            license_plate = input("License plate: ")
            carFee = x.check_out(license_plate)
            print(x.check_out(license_plate))
            if carFee:
                print("Parking fee: {:.2f} EUR".format(carFee))
            else:
                print("Could not find License plate")
        elif choice == "Q":
            quit()

if __name__ == "__main__":
    main()