class Order:
    """This represents order details placed by a customer (so, order ID, the customer themselves, their items, order-date, and their total."""

    #Constructor for order with their order ID, customer, and order date, all total.
    def __init__(self, order_id, customer, order_date):
        self.__order_id = order_id
        self._customer = customer
        self._items_list = []
        self._order_date = order_date
        self.__total_amount = 0.0


    #fucntions to add Ebook to the order list and updates the total price.
    def add_item(self, ebook):
        self._items_list.append(ebook) #update the ebook list
        self.__total_amount += ebook.get_price() #add to the total price

    #removes Ebook, just filtering out the ebook based on the isbn of the ebook
    def remove_item(self, isbn):
        self._items_list = [item for item in self._items_list if item.get_details()["isbn"] != isbn] #if the ebook is in the item list, it will be removed.

    #Function to calculates the total amount of the order from the item list
    def calculate_total_amount(self):
        return sum(item.get_price() for item in self._items_list) #using the sum(), this returns the price of each other ebooks in the item list


    #after all that, here, the function summarizes the order detail (Order's ID, customer, and the total in AED.
    def get_order_summary(self):
        return f"Order ID: {self.__order_id}, Customer: {self._customer.get_name()}, Total: {self.__total_amount} AED"


    #returns the order detail as a string
    def __str__(self):
        return self.get_order_summary()
