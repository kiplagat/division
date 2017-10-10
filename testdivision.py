import unittest
from division import division
class testdivision(unittest.TestCase):
     def test_answer_is_correct(self):
         self.assertEqual(division(8,4),2)
if __name__ == "_main__":
 unittest.main()
