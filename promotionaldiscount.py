# just to call back to the parent class (discount), so i can use their attributes in this subclass
from discount import Discount

class PromotionalDiscount(Discount):
    """This class would represent one aspect of the discount, in the case of promotional discount for orders. Only when the customer met with certain conditions"""
    #Constructor for
    def __init__(self, items_in_a_bundle = 5, discount_bundle_fee = 20):
        # using, super(), i am calling back the attributes of the discount to here.
        super().__init__(discount_bundle_fee) # 20% discount
        self._items_in_a_bundle = items_in_a_bundle  # this is items in bundle promotion = 5


    #Function to apply the discount (from the previous discount file).
    def apply_bundle_promo(self, order):
        # Here it check if the order has enough items to be allowed to consider for a promotional discount.
        if self.check_bundle_promo(order):
            total_with_discount = order.calculate_total_amount() * (1 - self._discount_fee / 100)
            return total_with_discount
        else:
            return order.calculate_total_amount() #resturns with the total discount of the order

    #checks if it qualifies for the bundle promo
    def check_bundle_promo(self, order):
        return len(order._items_list) >= self._items_in_a_bundle #returns true if it meets the requirement of a bundle promo


