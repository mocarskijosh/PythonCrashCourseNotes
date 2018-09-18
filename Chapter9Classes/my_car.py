# Tells Python to open the car module and import the class Car
#from car import Car

# Importing the entire module will make it easier to read and you don't have to worry about naming conflicts
import car

my_new_car = car.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()