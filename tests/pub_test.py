import unittest

from classes.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub(1000, ['Tennets'])
    
    def test_pub_has_name(self):
        self.assertEqual('The Royal Mile', self.pub.name)
    
    def test_pub_has_funds(self):
        self.assertEqual(1000, self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(['Tennets'], self.pub.drinks)