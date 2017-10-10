import unittest
from division import division
class testdivision(unittest.TestCase):
     def test_answer_is_correct(self):
         self.assertEqual(division(8,4),2)
     def test_result_is_not_infinite(self):
	     self.assertEqual(TypeError,division(8,0),"infinite")
if __name__ == "_main__":
 unittest.main()
