import unittest
from  src.calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(20,add(9,11))
    
    def test_subtract(self):
        self.assertEqual(6,subtract(10,4))

    def test_divide(self):
        self.assertEqual(10,divide(20,2))
    
    def test_multiply(self):
        self.assertEqual(6,multiply(2,3))
        

    
        
        