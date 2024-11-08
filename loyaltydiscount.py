# calls back from the parent class's attribute (discount) to be used in this other subclass.
from discount import Discount

class LoyaltyDiscount(Discount):
    """This class represents the other half of the discount class which is the loyalty discount. This would only be applied if they are a member of the websites loyalty program."""
    #Herem the constructor the loyalty discount only to those who are members with attributes (member rate)
    def __init__(self, loyalty_mem_rate):
        super().__init__(loyalty_mem_rate)

    def apply_loyalty_mem_rate(self, customer, order):
        # Here, if-statemet where it check if the customer is a loyalty member
        if customer.is_loyal_member():
            return order.calculate_total_amount() * 0.9  # if, yes it applies the 10% discount
        return order.calculate_total_amount()

    #also, here there is a bundle promotion for loyalty members as well.
    def check_bundle_promo(self, customer): #checks if there is a bundle promo that can be applied here.
        return customer.is_loyal_member() #returns if this is true that the member customer is qualified for the bundle

