# Each instance created from the Dog class will store a name and an age
#   also will give the dog the ability to sit() and roll_over()
class Dog(object):
    """A simple attempt to model a dog."""

    # This runs automatically whenever we create a new instance based on the Dog class
    # Every method call associated with a class automatically passes self, which is a reference
    #   to the instance itself. Gives individual instance access to the attributes and methods in the class.
    # self is ALWAYS PASSED!!!
    def __init__(self, name, age):
        """Initialize name and age attributes."""

        # Any variable prefixed with self is available to all methods in the class
        # Variables that are accessible through instances are called attributes
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + "rolled over!")

# Naming convention:
#   assume that capitalized names like Dog refer to a class
#   lowercase refer to single instance created from a class
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
#my_dog.roll_over()

# Creating Multiple Instances 
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
#your_dog.roll_over()