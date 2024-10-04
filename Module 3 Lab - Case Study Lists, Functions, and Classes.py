class Vehicle:
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    year = input("Please enter the year of the Vehicle: ")
    make = input("Please enter the make of the Vehicle: ")
    model = input("Please enter the model of the Vehicle: ")
    doors = input("Please enter the amount of doors on the vehicle: ")
    roof = input("Please enter if the vehicle has a Solid or Sun roof: ")

    vehicle = Vehicle(year, make, model, doors, roof)

    print("Vehicle year: ", vehicle.year)
    print("Vehicle make: ", vehicle.make)
    print("Vehicle model: ", vehicle.model)
    print("Vehicle doors: ", vehicle.doors)
    print("Vehicle roof type: ", vehicle.roof)

main()
