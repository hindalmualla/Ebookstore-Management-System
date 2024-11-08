#just calling back to the person file (I would need the attributes to be added here).
from person import Person


class Customer(Person):
    """this class would represents a customer (inherits attributes from person class from previous file"""

    # This is the constructor for which includes attributes from person, and adding new attributes (customer's ID, and if they have a membership).
    def __init__(self, name, email, phonenumber, customer_id = 0, is_loyal_member=False):
        super().__init__(name, email, phonenumber) #using super () method to call back the attributes from person class
        self.__customer_id = customer_id #added attribute 1
        self._is_loyal_member = is_loyal_member #added attribute 2

    #setter and getter for the attributes (applicable when needed)
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def is_loyal_member(self):
        return self._is_loyal_member

    def set_is_loyal_member(self, is_loyal_member):
        self._is_loyal_member = is_loyal_member

    #Here, I am using the __str__ to return the customer's information as a string
    def __str__(self):
        return f"{super().__str__()}, Customer ID: {self.__customer_id}, Loyalty Member: {self._is_loyal_member}"
