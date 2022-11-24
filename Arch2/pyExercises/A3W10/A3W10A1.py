from datetime import datetime
from datetime import datetime, timedelta

class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger():
    def check_in(self, license_plate,machineName, time) -> str:
        #We need to get sum data :) but from where? the parking machine ofcourse
        saveData = f'{time};cpm_name={machineName};license_plate={license_plate};action=check-in\n'

        #09-02-2022 14:33:54;cpm_name=North;license_plate=SG-123-B;action=check-in
        #23-11-2022 21:10:06;cpm_name=North;license_plate=xxxx;action=check_in
        try:
            with open("carparklog.txt", "a") as my_file:
                my_file.write(saveData)
        except:
            with open("carparklog.txt", "w") as my_file:
                my_file.write(saveData)
        
        
        return saveData

    def check_out(self, license_plate,machineName, parkingfee, time = datetime.now()) -> str:
        # 09-02-2022 16:50:02;cpm_name=North;license_plate=SG-123-B;action=check-out;parking_fee=6
        formatT = time.strftime("%d-%m-%Y %H:%M:%S")
        saveData = f'{formatT};cpm_name={machineName};license_plate={license_plate};action=check-out;parking_fee={parkingfee}\n'
        try:
            with open("carparklog.txt", "a") as my_file:
                my_file.write(saveData)
        except:
            with open("carparklog.txt", "w") as my_file:
                my_file.write(saveData)
        
        return saveData


class CarParkingMachine():
    parked_cars = {}

    def __init__(self, id='North', capacity=10, hourly_rate=2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.id = id
        self.carParkingLogger = CarParkingLogger()
    def check_in(self, license_plate , time = datetime.now()):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, time)
            #cleanup time 
            formatT = time.strftime("%d-%m-%Y %H:%M:%S")
            return self.carParkingLogger.check_in(license_plate, self.id, formatT)
        else:
            return False

    def check_out(self, license_plate):
        if license_plate in self.parked_cars:
            #return self.get_parking_fee(license_plate)
            fee = self.get_parking_fee(license_plate)
            self.carParkingLogger.check_out(license_plate, self.id, fee)
            return self.hourly_rate
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

def main():
    x = CarParkingMachine('North', 10, 2.5)
    cpm = CarParkingMachine(id="North",capacity=2, hourly_rate=4.0)
    cpm.check_in("BB-494-H")
    cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))

    print(cpm.hourly_rate)
    print(cpm.check_out("BB-494-H"))
    while True:
        print("""
                [I] Check-in car by license plate
                [O] Check-out car by license plate
                [Q] Quit program
                """)
        choice = input("Choose an option: ").upper()
        if choice == "I":
            license_plate = input("License plate: ")
            if len(license_plate) > 3:
                print(x.check_in(license_plate))
            else:
                print("Capacity reached!")
        elif choice == "O":
            license_plate = input("License plate: ")
            carFee = x.check_out(license_plate)
            if carFee:
                print(x.check_out(license_plate))
            else:
                print("Could not find License plate")
        elif choice == "Q":
            quit()

if __name__ == "__main__":
    main()