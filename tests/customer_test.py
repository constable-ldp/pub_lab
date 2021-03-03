import unittest
from classes.customer import Customer
from classes.drinks import Drinks
from classes.pub import Pub


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Luke', 50.00, 18, 0)
        self.drinks = Drinks('Tennents', 1.50, 100, 3)
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

    def test_buy_drinks__pass(self):
        self.customer.buy_drinks(self.drinks, self.pub, self.customer)
        self.assertEqual(48.50, self.customer.wallet)
        self.assertEqual(1001.50, self.pub.till)
        self.assertEqual(3, self.customer.drunkenness)

    def test_buy_drinks__fail_underage(self):
        customer = Customer('Anakin', 40.00, 16, 0)
        self.assertEqual(None, self.customer.buy_drinks(self.drinks, self.pub, customer))

    def test_buy_drinks__fail_drunk(self):
        customer = Customer('Leia', 25.00, 19, 11)
        self.assertEqual(None, self.customer.buy_drinks(self.drinks, self.pub, customer))

    def test_buy_drinks__fail_skint(self):
        customer = Customer('Obi Wan', 1.00, 19, 3)
        self.assertEqual(None, self.customer.buy_drinks(self.drinks, self.pub, customer))