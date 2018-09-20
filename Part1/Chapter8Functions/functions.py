# Chapter 8 Functions

'''
# Store functions in separate files called modules to help organize the main program

# Def a function

def greetUser():
    """Display a simple greeting."""
    print("Hello!")

greetUser()


# Passing Information to a Function

def greetUser(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greetUser('jessie')



# In addition to calling functions normally, you can also call a function like the following
# This is called Keyword Arguments

def describePet(animalType, petName):
    """Display information about a pet."""
    print("\nI have a " + animalType + ".")
    print("My " + animalType + "'s name is " + petName.title() + ".")

describePet(animalType='hamster', petName='harry')

=>
$ python functions.py

I have a hamster.
My hamster's name is Harry.




# Default Values

def describePet(petName, animalType = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animalType + ".")
    print("My " + animalType + "'s name is " + petName.title() + ".")

describePet('willie')

=>
$ python functions.py

I have a dog.
My dog's name is Willie.



# Returning a Dictionary

def buildPerson(fname, lname):
    """Return a dictionary of information about a person."""
    person = {'first': fname, 'last': lname}
    return person

musician = buildPerson('jimi', 'hendrix')
print(musician)

=>
$ python functions.py
{'first': 'jimi', 'last': 'hendrix'}



# Preventing a Function from Modifying a List

# sending a copy of a list to a function.....
# functionName(listName[:])



# Passing an Arbitrary Number of Arguments

def makePizza(*toppings):
    """Printing the list of toppings that have been requested."""
    print(toppings)

makePizza('pepperoni')
makePizza('mushrooms', 'green peppers', 'extra cheese')

=>
$ python functions.py
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')

# this is also valid
def makePizza(size, *toppings):
    ~~~~~

makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Passing Key-Value Pairs as Function Arguments

def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['firstName'] = first
    profile['lastName'] = last

    for key, value in userInfo.items():
        profile[key] = value
    return profile

userProfile = buildProfile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(userProfile)

=>
$ python functions.py
{'firstName': 'albert', 'lastName': 'einstein', 'location': 'princeton', 'field': 'physics'}

'''

