# Using the Python Standard Library

# import OrderedDict from the module collections....
# OrderedDict will keep track of the order in which key-value pairs are added
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")