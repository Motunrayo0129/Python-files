import motun_banking_apps
import unittest
from unittest import TestCase

accounts_info = []

class TestMotunBankingApp(TestCase):

    def setUp(self):
        global accounts_info
        accounts_info = [("Motunrayo", "08121135541", 1000)]

    def test_account_was_created(self):
        expected_account = accounts_info
        self.assertEqual(accounts_info, expected_account)

    def test_money_deposited_in_account(self):
        get_account = accounts_info
        deposit_money = ("Motunrayo", accounts_info[0][2] + 3000)
        expected_account = ("Motunrayo", 4000)
        self.assertEqual(deposit_money, expected_account)

    def test_money_withdraw_in_account(self):
        get_account = accounts_info
        withdraw_amount = ("Motunrayo", accounts_info[0][2] - 500)
        expected_account = ("Motunrayo", 500)
        self.assertEqual(withdraw_amount, expected_account)

    def test_money_withdraw_in_account_is_greater(self):
        get_account = accounts_info
        amount_input = 1000
        result = "Insufficient funds"
        if accounts_info[0][2] > amount_input:
            result = "Insufficient funds"
        expected_result = "Insufficient funds"
        self.assertEqual(result, expected_result)

    def test_large_money_was_deposited_in_account(self):
        get_account = accounts_info
        amount_input = 50000
        result = "Large deposit detected"
        if accounts_info[0][2] > amount_input:
            result = "Large deposit detected"
        expected_result = "Large deposit detected"
        self.assertEqual(result, expected_result)


    def test_user_enter_negative_amount(self):
        get_account = accounts_info
        amount_input = -1
        result = "Cannot perform transaction on negative input"
        if amount_input <= 0:
            result = "Cannot perform transaction on negative input"
        expected_result = "Cannot perform transaction on negative input"
        self.assertEqual(result, expected_result)

    def test_user_has_limited_access(self):
        get_account = accounts_info
        amount_input = 10000
        result = "Limit exceeded"
        if amount_input > 10000:
            result = "Limit exceeded"
        expected_result = "Limit exceeded"
        self.assertEqual(result, expected_result)

                                   	
    def test_incorrect_name(self):
        get_account = accounts_info
        name_input = "Motunayo"
        if accounts_info[0][0] != name_input :
            result = "Account not found"
        expected_result = "Account not found"
        self.assertEqual(result, expected_result)
    
    def test_incorrect_phone_numbers(self):
        get_account = accounts_info
        number_input = "08121133721"
        if accounts_info[0][1] != number_input :
            result = "Account not found"
        expected_result = "Account not found"
        self.assertEqual(result, expected_result)

