import unittest
from pricing import total

class PricingTest(unittest.TestCase):
    def test_total(self):
        self.assertAlmostEqual(total(10.1), 12.12)
