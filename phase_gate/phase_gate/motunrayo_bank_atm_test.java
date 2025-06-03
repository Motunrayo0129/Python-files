import motunrayo_bank_atm
import unittest
from unittest import TestCase


class TestAccount(TestCase):
	def test_that_get_bank_exist(self):
		motunrayo_bank_atm.deposit_amount(balance)

	def test_that_account_function_return_correct_answer(self):
		balance = 1000
		actual = motunrayo_bank_atm.withdrawn_amount(1000)
		expected = 1000
		self.assertEqual(actual, expected)
		
