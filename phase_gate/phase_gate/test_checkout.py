import unittest
from check_out_app import *

class TestCheckout(unittest.TestCase):

    def test_calculate_totals(self):
        subtotal = 100.0
        discount, vat, total = calculate_totals(subtotal, 10)  
        self.assertEqual(discount, 10.0)  
        self.assertEqual(vat, 7.5)        
        self.assertEqual(total, 97.5)

    def test_get_items(self):
        products = [("Apple", 2.0, 3), ("Banana", 1.5, 2)]
        items, subtotal = get_items(products)
        expected_subtotal = (2.0 * 3) + (1.5 * 2)
        self.assertEqual(subtotal, expected_subtotal)  
        self.assertEqual(len(items), 2)

    def test_process_amount(self):
        subtotal = 5900
        discount_rate = 10
amount_paid = 6000
        discount, vat, total = calculate_totals(subtotal, 10)  
  	balance = amount_paid - total
        self.assertEqual(balance, 6000 - total, places = 2)  
              
        
