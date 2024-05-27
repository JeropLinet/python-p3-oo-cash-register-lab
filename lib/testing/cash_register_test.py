#!/usr/bin/env python3

import io
import sys
import unittest
from cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    '''CashRegister in cash_register.py'''

    def setUp(self):
        self.cash_register = CashRegister()
        self.cash_register_with_discount = CashRegister(20)

    def tearDown(self):
        self.reset_register_totals()

    def reset_register_totals(self):
        self.cash_register.total = 0
        self.cash_register_with_discount.total = 0

    def test_discount_attribute(self):
        '''takes one optional argument, a discount, on initialization.'''
        self.assertEqual(self.cash_register.discount, 0)
        self.assertEqual(self.cash_register_with_discount.discount, 20)

    def test_total_attribute(self):
        '''sets an instance variable total to zero on initialization.'''
        self.assertEqual(self.cash_register.total, 0)
        self.assertEqual(self.cash_register_with_discount.total, 0)

    def test_items_attribute(self):
        '''sets an instance variable items to empty list on initialization.'''
        self.assertEqual(self.cash_register.items, [])
        self.assertEqual(self.cash_register_with_discount.items, [])

    def test_add_item(self):
        '''accepts a title and a price and increases the total.'''
        self.cash_register.add_item("eggs", 0.98)
        self.assertEqual(self.cash_register.total, 0.98)

    def test_add_item_optional_quantity(self):
        '''also accepts an optional quantity.'''
        self.cash_register.add_item("book", 5.00, 3)
        self.assertEqual(self.cash_register.total, 15.00)

    def test_add_item_with_multiple_items(self):
        '''doesn't forget about the previous total'''
        self.cash_register.add_item("Lucky Charms", 4.5)
        self.cash_register.add_item("Ritz Crackers", 5.0)
        self.cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
        self.assertEqual(self.cash_register.total, 14.5)

    def test_apply_discount(self):
        '''applies the discount to the total price.'''
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()   
        self.assertEqual(self.cash_register_with_discount.total, 800)

    def test_apply_discount_success_message(self):
        '''prints success message with updated total'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "After the discount, the total comes to $800.00.\n")

    def test_apply_discount_reduces_total(self):
        '''reduces the total'''
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        self.assertEqual(self.cash_register_with_discount.total, 800)

    def test_apply_discount_when_no_discount(self):
        '''prints a string error message that there is no discount to apply'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register.apply_discount()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "There is no discount to apply.\n")

    def test_items_list_without_multiples(self):
        '''returns an array containing all items that have been added'''
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99)
        new_register.add_item("tomato", 1.76)
        self.assertEqual(new_register.items, ["eggs", "tomato"])

    def test_items_list_with_multiples(self):
        '''returns an array containing all items that have been added, including multiples'''
        new_register = CashRegister()
        new_register.add_item("eggs", 1.99, 2)
        new_register.add_item("tomato", 1.76, 3)
        self.assertEqual(new_register.items, ["eggs", "eggs", "tomato", "tomato", "tomato"])

def test_void_last_transaction(self):
    '''subtracts the last item from the total'''
    self.cash_register.add_item("apple", 0.99)
    self.cash_register.add_item("tomato", 1.76)
    self.cash_register.void_final_item()
    self.assertEqual(self.cash_register.total, 0.99)  # Expected total after voiding last item

def test_void_last_transaction_with_multiples(self):
    '''returns the total to 0.0 if all items have been removed'''
    self.cash_register.add_item("tomato", 1.76, 2)
    self.cash_register.void_final_item()
    self.assertEqual(self.cash_register.total, 0.0)  # Adjust expected value if needed


if __name__ == "__main__":
    unittest.main()
