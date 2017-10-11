import unittest
from division import division
class testdivision(unittest.TestCase):
     def test_answer_is_correct(self):
         self.assertEqual(division(8,4),1)
     def test_answer_works_for_negative(self):
	     self.assertEqual(division(-25,-5),5)
     def test_result_is_not_infinite(self):
	     self.assertRaises(TypeError)
if __name__ == "__main__":
 unittest.main()
