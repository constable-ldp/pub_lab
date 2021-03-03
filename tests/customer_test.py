import unittest
from classes.customer import Customer
from classes.drinks import Drinks
from classes.pub import Pub


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Luke', 50.00, 18)
        self.drinks = Drinks('Tennents', 1.50, 100)
        self.pub = Pub( "till you drop", 1000, [self.drinks])

    def test_has_name(self):
        self.assertEqual('Luke', self.customer.name)

    def test_has_price(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(18, self.customer.age)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drinks)
        self.assertEqual(48.50, self.customer.wallet)

    def test_buy_drinks(self):
        self.customer.buy_drinks(self.drinks, self.pub)
        self.assertEqual(48.50, self.customer.wallet)
        self.assertEqual(1001.50, self.pub.till)
