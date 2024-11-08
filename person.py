class Person:
    """This class represents a potential customer, just a person that contain general contact details """

    # This is the constructor for which includes attributes like name, email, phone
    def __init__(self, name = "", email = "", phonenumber = ""):
        self.__name = name
        self.__email = email
        self.__phonenumber = phonenumber

    # the getters (for name, email, and phone)
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phonenumber(self):
        return self.__phonenumber

    # the setters (for name, email, and phone number)
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    # This is the string method that I want to return it as a string
    def __str__(self):
        return f"Name: {self.__name}, Email: {self.__email}, Phone: {self.__phonenumber}"
