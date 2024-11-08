# Import necessary classes from the modules
from ebook import Ebook
from catalog import Catalog
from person import Person
from customer import Customer
from shoppingcart import ShoppingCart
from order import Order
from discount import Discount
from loyaltydiscount import LoyaltyDiscount
from promotionaldiscount import PromotionalDiscount
from payment import Payment
from reciept import Receipt

def main():
    # starting off with the catalog:
    catalog = Catalog()

    # Test 1:
    print("Test 1: Adding a new e-book to the catalog")
    ebook1 = Ebook(title="The Silmarillion", author="J.R.R. Tolkien", genre="Fantasy", pub_date="1977-09-15", price=.35, isbn="ISBN001")
    catalog.add_ebook(ebook1)
    print(catalog)

    # Test 2:
    print("\nTest 2: Modifying the e-book to catalog")
    ebook1.set_price(45.0)  # Modify the price
    print(catalog)

    # Test 3:
    print("\nTest Case 3: Remove an e-book from the catalog")
    catalog.remove_ebook("ISBN12345")
    print(catalog)

    # Here, I am re-adding the e-book to test further
    catalog.add_ebook(ebook1)

    # Test 4:
    print("\nTest Case 4: Adding new customer")
    customer1 = Customer(name="Hind Almualla", email="20225553336@zu.ae", phonenumber="0506664477", customer_id=1, is_loyal_member=True)
    print(customer1)

    # Test 5:
    print("\nTest Case 5: Modifying the customer's account detail")
    customer1.set_email("20327776781@zu.ae")
    print(customer1)

    # Test 6:
    print("\nTest 6: Remove customer account")
    customer1 = None
    print("Customer account is removed.")

    # Here, I am re-adding the customer to test further
    customer1 = Customer(name="Hind Almualla", email="20327776781@zu.ae", phonenumber="0506664477", customer_id=1, is_loyal_member=True)

    # Test 7:
    print("\nTest 7: Adding e-books to the shopping cart")
    ebook2 = Ebook(title="A Feast for Crows", author="George R.R. Martin", genre="Sci-Fi Fantasy", pub_date="1996-08-06", price=65.0, isbn="ISBN002")
    catalog.add_ebook(ebook2)
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(ebook1)
    shopping_cart.add_item(ebook2, quantity=2)
    print(shopping_cart)
    print(f"Total cart value: {shopping_cart.calculate_total()} AED")

    # Test Case 8:
    print("\nTest 8: Applying discounts for loyal members")
    order = Order(order_id=1001, customer=customer1, order_date="2023-10-10")
    order.add_item(ebook1)
    order.add_item(ebook2)
    loyalty_discount = LoyaltyDiscount(loyalty_mem_rate=10)  # 10% discount
    total_after_loyalty_discount = loyalty_discount.apply_the_discount(order)
    print(f"The total with the loyalty discount: {total_after_loyalty_discount} AED")

    # Test 9:
    print("\nTest 9: Applying discounts for bundled/promo purchases")
    promotional_discount = PromotionalDiscount(items_in_a_bundle=5, discount_bundle_fee=20)  # 20% discount
    total_after_promo_discount = promotional_discount.apply_the_discount(order)
    print(f"Total after promotional discount: {total_after_promo_discount} AED")

    # Test 10:
    print("\nTest 10: Generating an invoice")
    # Here just applying both of the discounts choices (promo and loyalty)
    discounts = [loyalty_discount, promotional_discount]
    payment = Payment(order)
    final_total = payment.calculate_final_payment(discounts)
    print(f"Final total after all the discounts: {final_total} AED")
    payment.process_payment()

    receipt = Receipt(receipt_id=10112, order=order, payment=payment)
    receipt.display_receipt()

if __name__ == "__main__":
    main()
