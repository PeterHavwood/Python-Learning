class Vehicle(object):
    def run(self):
        print('Vehicle is running...')

class Car(Vehicle): # Inherited from vehicle
    # Override
    def run(self):
        print('Car is running on road...')

class Dog(object):
    def run(self):
        print('Dog is running...wolf!')

def run_twice(vehicle):
    vehicle.run()
    vehicle.run()

# How polymorphism works
run_twice(Vehicle())
run_twice(Car())
# Python is a dynamic language
# Which means you can pass an instance not in vehicle tye(only need run() function)
run_twice(Dog())
