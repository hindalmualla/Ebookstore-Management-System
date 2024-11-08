class Discount:
    """This would represent the class for discounts where it would be applicable for the customer's orders."""

    # Constructor for the discount fees
    def __init__(self, discount_fee = 0.0):
        self._discount_fee = discount_fee  # Protected

    # Function where it sets default of 'no discount' being applied.
    def apply_the_discount(self, order):
        return order.calculate_total_amount()  # returns order's total without the discount

    # Using the getter, it returns the discount fee percentage
    def get_discount_fee(self):
        return self._discount_fee

