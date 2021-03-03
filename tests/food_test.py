import unittest

from classes.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food ('Fish and Chips', 2.50, 3)

    def test_has_name(self):
        self.assertEqual('Fish and Chips', self.food.name)

    def test_has_price(self):
        self.assertEqual(2.50, self.food.price)

    def test_has_rejuvenation_abilities(self):
        self.assertEqual(3, self.food.rejuvenation_level)