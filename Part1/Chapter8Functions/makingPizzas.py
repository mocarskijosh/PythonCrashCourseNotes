# This will import everything from the other file
#import pizza
# you can also give the module above ^^ an alias

# This will import only specific functions
#from pizza import makePizza

# This will import only specific functions with an alias
from pizza import makePizza as pie


#pizza.makePizza(16, 'pepperoni')
#pizza.makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#makePizza(16, 'pepperoni')
#makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')

pie(16, 'pepperoni')
pie(12, 'mushrooms', 'green peppers', 'extra cheese')


'''
=>
$ python makingPizzas.py

Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
'''