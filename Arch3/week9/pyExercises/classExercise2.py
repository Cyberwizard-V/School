class Car:
    def __init__(self, model, licenseplate, brand):
        self.model = model
        self.licenseplate = licenseplate
        self.brand = brand

    def validateLP(self):
        if len(self.licenseplate) < 6:
            return "valid"
        else:
            return "Invalid"

    def weLoveCars(self):
        if self.validateLP() == "valid":
            print(f""""
            Car model: {self.model}
            Licenseplate: {self.licenseplate}
            Brand: {self.brand}
            """)
        else:
            return "ERROR: License plate is wrong"

xCar = Car("test", "1233", "test")
print(xCar.weLoveCars())





