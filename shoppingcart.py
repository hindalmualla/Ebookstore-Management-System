class ShoppingCart:
    """This class is representing the shopping cart where customers would add their orders (ebooks) here before proceeding with checkout ."""

    #constructor for shopping cart where it contains items (ebooks)
    def __init__(self):
        self._items = {} # as a dict

    #method to add items yto the shopping cart
    def add_item(self, ebook, quantity=1): #note: it adds quantity when an ebook is already in the cart
        #using if-statement,
        if ebook in self._items:
            #if ebook is in the cart, it increments the quantity
            self._items[ebook] += quantity
        else:
            self._items[ebook] = quantity #if not in the cart, it adds to the specified number (quanity)

    #method for removing items from the shopping cart
    def remove_item(self, ebook): #ebook (object) to be removed from the cart
        if ebook in self._items:
            #remove = using del function to delete that ebook from the dictionary if it was already in the cart
            del self._items[ebook]

    #method to calculate the total cost of all the items within the cart
    def calculate_total(self):
        #return the sum of the all the ebooks in the shopping cart
        return sum(ebook.get_price() * quantity for ebook, quantity in self._items.items())

    #using the string method, it would return the items in the shopping cart and their amount as a string.
    def __str__(self):
        return "Shopping Cart:\n" + "\n".join(f"{ebook}: {quantity}" for ebook, quantity in self._items.items())
