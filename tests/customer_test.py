import unittest
from classes.customer import Customer
from classes.drinks import Drinks

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Luke Constable', 50.00)
        self.drinks = Drinks('Tennents', 1.50, 100)

    def test_has_name(self):
        self.assertEqual('Luke Constable', self.customer.name)

    def test_has_price(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drinks)
        self.assertEqual(48.50, self.customer.wallet)
