import unittest

from string_calculator import add

class TestStringCalculator(unittest.TestCase):

  def test_empty_string(self):
    self.assertEqual(add(""), 0)

  def test_comma(self):
    self.assertEqual(add("1"), 1)
    self.assertEqual(add("1,2"), 3)

  def test_newlines(self):
    self.assertEqual(add("1\n2,3"), 6)
    self.assertRaises(ValueError, add, "1,\n")

  def test_delimeter(self):
    self.assertEqual(add("//;\n1;2;3;4"), 10)
    self.assertEqual(add("//*\n1*2*3*4"), 10)
    self.assertRaises(ValueError, add, "//*\n1*\n")

  def test_negatives(self):
    self.assertRaises(ValueError, add ,"1,-2")
    self.assertRaises(ValueError, add ,"//*\n1*-2")

    try:
      add("1,-2,3")
    except ValueError as e:
      self.assertEqual(str(e), 'negatives not allowed. found -2')

  def test_numbers_bigger_than_thousand(self):
    self.assertEqual(add('2,1001,3'), 5)
    self.assertEqual(add('//;\n1003;1001;1005'), 0)

  def test_delemeter_more_than_one_length(self):
    self.assertEqual(add('//;;\n1;;2;;3'), 6)
    self.assertEqual(add('//***\n1***2***3***1001'), 6)
    self.assertRaises(ValueError, add, '//***\n1***2***3***')
    self.assertRaises(ValueError, add, '//***\n1***2\n3***')

  def test_multiple_types_of_delemeter(self):
    self.assertEqual(add('//[;][%]\n1;2%3\n4'), 10)
    self.assertEqual(add('//[;][%]\n1;2%3\n4%1001;2'), 12)

  def test_multiple_types_of_delemeters_of_multiple_length(self):
    self.assertEqual(add('//[;;][%][***]\n1;;2%3***4%1000'), 1010)
    self.assertEqual(add('//[;;][%][***]\n1;;2%3***4%1000\n5'), 1015)