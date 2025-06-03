import motunrayo_bank_atm
import unittest
from unittest import TestCase


class TestAccount(TestCase):
	def test_that_get_bank_exist(self):
		motunrayo_bank_atm.deposit_amount(1000)

	def test_that_account_function_return_correct_answer(self):
		balance = 1000
		deposit = 1000
		new_amount = 2000
		actual = motunrayo_bank_atm.deposit_amount(balance + deposit, new_amount)
		expected = 2000
		self.assertEqual(actual, expected)
		
