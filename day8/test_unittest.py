import unittest
from doctestdemo import equals

class test_equals(unittest.TestCase):
  def test_can_add_num(self):
      self.assertEqual(equals(8,8), "Equal")

  def test_not_equals(self):
      self.assertEqual(equals(-2,-4), "Not Equal")


if __name__ == '__main__':
    unittest.main()