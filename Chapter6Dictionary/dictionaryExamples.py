#Dictionary

'''
#
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#=> green
#=> 5

# These are all key value pairs!

# You can store any python object as a value!

# Adding to a blank one
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#=> {'color': 'green', 'points': 5}

#
favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " +
    favoriteLanguages['sarah'].title() +
    ".")

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

=>
    Key: username
    Value: efermi

    Key: first
    Value: enrico

    Key: last
    Value: fermi
    

favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favoriteLanguages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

=>
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.



# Looping Through All the Keys in a Dictionary

favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# could have also left off the .keys() as it is default behavior to do this 
# so it would have been just favoriteLanguages
for name in favoriteLanguages.keys():
    print(name.title())

=>
Jen
Sarah
Edward
Phil


# Loop through the keys in order

for name in sorted(favoriteLanguages.keys()):
    print(name.title() + ", thank you for taking the poll.")

=>
    All sorted in a-z on the key!



# Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

=>
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

=>
$ python dictionaryExamples.py
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
Total number of aliens: 30


# List in a Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order. 
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for toppings in pizza['toppings']:
    print("\t" + toppings)

=>
You ordered a thick-crust pizza with the following toppings:
        mushrooms
        extra cheese

# Example
favoriteLanguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favoriteLanguages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

=>
$ python dictionaryExamples.py

Jen's favorite languages are:
        Python
        Ruby

Sarah's favorite languages are:
        C

Edward's favorite languages are:
        Ruby
        Go

Phil's favorite languages are:
        Python
        Haskell

# Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, userInfo in users.items():
    print("\nUsername: " + username)
    fullName = userInfo['first'] + " " + userInfo['last']
    location = userInfo['location']

    print("\tFull Name: " + fullName.title())
    print("\tLocation: " + location.title())

=>
$ python dictionaryExamples.py

Username: aeinstein
        Full Name: Albert Einstein
        Location: Princeton

Username: mcurie
        Full Name: Marie Curie
        Location: Paris

'''
