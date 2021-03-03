import unittest

from classes.pub import Pub
from classes.drinks import Drinks
from classes.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks('Tennents', 1.50, 100, 3)
        self.pub = Pub('The Royal Mile', 1000.00, [self.drinks])
        self.customer = Customer('Luke', 50.00, 18, 0)
    
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
        new_drink = Drinks('Gin and Tonic', 2.50, 100, 1.5)
        self.pub.add_new_drink(new_drink)
        self.assertEqual(2, len(self.pub.drinks))
    
    def test_check_underage__true(self):
        customer = Customer('Vitor', 100.00, 17, 0)
        self.assertEqual(True, self.pub.check_underage(customer))

    def test_check_underage__false(self):
        self.assertEqual(False, self.pub.check_underage(self.customer))

