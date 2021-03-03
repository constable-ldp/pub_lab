import unittest
from classes.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks('Tennents', 1.50)

    def test_has_name(self):
        self.assertEqual('Tennents', self.drinks.name)

    def test_has_price(self):
        self.assertEqual(1.50, self.drinks.price)