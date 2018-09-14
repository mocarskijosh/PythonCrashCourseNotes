# Chatper 7: User Input and While Loops
'''
# Using input()

message = input("Tell me something, and I will repeast it back to you: ")
print(message)


# While Loop
currentNumber = 1
while currentNumber <= 5:
    print(currentNumber)
    currentNumber += 1


# Using a while Loop with Lists and Dictionaries

# Never modify a list inside a FOR LOOP!!!! Python will have trouble keeping track of the items in the list
# Instead use a WHILE LOOP!

unconfirmedUsers = ['alice', 'brian', 'candace']
confirmedUsers = []

# Verify each user until there are no more unconfirmed users 
# Move each verified user into the list of confirmed users
while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()

    print("Verifying user: " + currentUser.title())
    confirmedUsers.append(currentUser)

# Display all confirmed users 
print("\nThe following users have been confirmed:")
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())

=>
$ python UserInputAndWhile.py
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice



# Remove all instances of a specific value from a list

pets = ['dog', 'cat', 'goldfish', 'rabbit', 'cat', 'zebra', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

=>
$ python UserInputAndWhile.py
['dog', 'cat', 'goldfish', 'rabbit', 'cat', 'zebra', 'cat']
['dog', 'goldfish', 'rabbit', 'zebra']

'''


