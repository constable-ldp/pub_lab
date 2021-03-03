import unittest

from classes.pub import Pub
from classes.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks('Tennents', 1.50, 100)
        self.pub = Pub(1000.00, [self.drinks])
    
    def test_pub_has_name(self):
        self.assertEqual('The Royal Mile', self.pub.name)
    
    def test_pub_has_funds(self):
        self.assertEqual(1000.00, self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual([self.drinks], self.pub.drinks)

    def test_pub_increase_till(self):
        self.pub.increase_till(self.drinks)
        self.assertEqual(1001.50, self.pub.till)

    def test_add_new_drink(self):
        new_drink = Drinks('Gin and Tonic', 2.50, 100)
        self.pub.add_new_drink(new_drink)
        self.assertEqual(2, len(self.pub.drinks))