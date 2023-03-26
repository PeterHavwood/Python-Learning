class Vehicle(object):
    def run(self):
        print('Vehicle is running...')

class Car(Vehicle): # Inherited from vehicle
    def __init__(self, model):
        self.__model = model

    def run(self):
        print('Car is running on road...')
    
# Use type()
print(f'type(123): {type(123)}')
str = 'hello world'
print(f'type(\'hello world\'): {type(str)}')
car = Car('TT')
print(f'type(Car): {type(Car)}')
print(f'type(Car(\'TT\')): {type(car)}')

# Use Instance()
print(isinstance(car,Car))
print(isinstance(car,Vehicle))

# Use dir()
print(dir(car))

# Use hasattr()
if hasattr(car,'run'):
    car.run()
else:
    print('Cant run!')