from typing import List
from discount import Discount


class Payment:
    """This class represents the customer's payment for their ebook orders."""

    # Constructor for the payment where it includes the order and the choice of payment method (credit card only)
    def __init__(self, order, payment_method="Credit Card"):
        self._order = order
        self._payment_method = payment_method
        self._total_payment = self.calculate_final_payment([])  # Initial total payment

    def process_payment(self):
        print(f"Processing payment of {self._total_payment} AED via {self._payment_method}.")

    def calculate_final_payment(self, discounts=None):
        total = self._order.calculate_total_amount()  # Get the original total amount
        if discounts:
            for discount in discounts:
                total = discount.apply_the_discount(self._order)  # Apply each discount and update total
        self._total_payment = total  # Store final total in the total_payment
        return total

    # As a string, it would return the payment amount as AED and type of payment method (credit card)
    def __str__(self):
        return f"Payment Amount: {self._total_payment} AED via {self._payment_method}"
