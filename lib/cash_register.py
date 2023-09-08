#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - (self.total - self.items[-1])
            self.total -= last_item_price
            self.items.pop()

# Uncomment the following lines to test the class independently
# cash_register = CashRegister()
# cash_register_with_discount = CashRegister(20)
# cash_register.add_item("eggs", 0.98)
# cash_register_with_discount.add_item("macbook air", 1000)
# cash_register_with_discount.apply_discount()
# cash_register_with_discount.void_last_transaction()
# print(cash_register.total)
# print(cash_register_with_discount.total)