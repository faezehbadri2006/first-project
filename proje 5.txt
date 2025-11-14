# Class-e Valed
class Vehicle:
    def init(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

# Class-e Farzand: Car
class Car(Vehicle):
    def init(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

# Class-e Farzand: Motorcycle
class Motorcycle(Vehicle):
    def init(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has Sidecar: {'Bale' if self.has_sidecar else 'Na'}")

# Sakht-e 3 shey az class-ha
vehicle1 = Vehicle("Honda", 2010)
car1 = Car("Toyota", 2022, 4)
motorcycle1 = Motorcycle("Yamaha", 2018, True)

# Farakhani-e method-ha
print("Vehicle:")
vehicle1.display_info()

print("\nCar:")
car1.display_info()

print("\nMotorcycle:")
motorcycle1.display_info()