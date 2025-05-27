import categorize_numbers
import unittest
from unittest import TestCase


class TestCategorizeNumbers(TestCase):
	def test_that_categorize_if_numbers_exists(self):
		categorize_numbers.get_numbers(5)

	def test_that_categorize_number_return_correct_answer(self):
		actual = categorize_numbers.get_numbers(20)
		expected = 20
		self.assertEqual(actual, expected)
		actual = categorize_numbers.get_numbers(15)
		expected = 15
		self.assertEqual(actual, expected)

	def test_that_get_numbers_function_work_for_number_divisible_by_5(self):
		self.assertEqual(categorize_numbers.get_numbers(12), "No divisible number found")



