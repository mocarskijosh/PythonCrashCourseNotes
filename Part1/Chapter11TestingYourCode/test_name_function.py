# unittest module is from the Python standard library, it provides testing tools
'''
Unit Test - 
    Verifies that one specific aspect of a function's behavior is correct
Test Case - 
    Collection of unit tests that together prove that a function behaves as it's supposed to 


Create a class that inherits from unittest.TestCase

'''

import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Admadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()