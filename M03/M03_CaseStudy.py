class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    print("Welcome to the Vehicle Information App!")
    print("Please enter the following details for your car:\n")
    
    # Initial car details input
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    
    # Input for Doors
    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ['2', '4']:
            break
        else:
            print("Please enter either '2' or '4'")
    
    # Roof Input
    while True:
        roof = input("Enter type of roof (solid or sun roof): ").lower()
        if roof in ['solid', 'sun roof']:
            break
        else:
            print("Please enter either 'solid' or 'sun roof'")
    
    # Create car object
    car = Automobile("car", year, make, model, doors, roof)
    
    # Display car information
    print("\n" + "="*40)
    print("VEHICLE INFORMATION")
    print("="*40)
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")
    print("="*40)

# Run the program
if __name__ == "__main__":
    main()