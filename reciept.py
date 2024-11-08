from order import Order
from payment import Payment


class Receipt:
    """This class represents the invoice/receipt generated for the customer's payment."""

    #constructor for the reciept which includes meantioned attributes
    def __init__(self, receipt_id, order, payment, discounted=None, VAT_fee=0.08):
        self._receipt_id = receipt_id
        self._order = order
        self._payment = payment
        self._discounted = discounted if discounted else []
        self._VAT_fee = VAT_fee

    #calculating with the VAT
    def calculate_VAT(self):
        total_amount = self._payment._total_payment
        VAT_amount = total_amount * self._VAT_fee
        return VAT_amount

    #what is gonna be generated as an invoice
    def invoice_statement(self):
        total_before_VAT = self._payment._total_payment
        VAT_amount = self.calculate_VAT()
        total_with_VAT = total_before_VAT + VAT_amount

        return (
            f"Receipt ID: {self._receipt_id}\n"
            f"Order ID: {self._order}\n"
            f"VAT ({self._VAT_fee * 100}%): {VAT_amount} AED\n"
            f"Total With VAT: {total_with_VAT} AED"
        )

    #here, it would display the invoice
    def display_receipt(self):
        print(self.invoice_statement())

    #As a string, this would generate the invoice statement simply.
    def __str__(self):
        return self.invoice_statement()