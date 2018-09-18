# Inheritance 

'''
When one class inherits from another, it automatically takes all of the attributes and methods of the first class.
Parent Class - The original class
Child Class - 
This is based on the Car class
'''
from car import Car

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # This is for Python 2.X
        #super(ElectricCar, self).__init__(make, model, year)

        # Using an Instance as Attributes
        self.battery = Battery()

    # Overriding
    """Def a method in the child class with the same name as the method you want to override in the parent class. """
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

# This doesn't inherit from anyother class
class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
#my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_beetle = Car('Volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())