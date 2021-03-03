import unittest
from classes.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Luke Constable', 50.00)

    def test_has_name(self):
        self.assertEqual('Luke Constable', self.customer.name)

    def test_has_price(self):
        self.assertEqual(50.00, self.customer.wallet)