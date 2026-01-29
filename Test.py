!/usr/bin/python3
import unittest
from Prog1 import summation
class Testsum(unittest.TestCase):
  def class_list_int(self):
    """
    Test case to add two numbers
    """
    data=[23,32]
    result=summation(data)
    self.assertEqual(result,55)
if __name__ == '__main__'
  unittest.main()
