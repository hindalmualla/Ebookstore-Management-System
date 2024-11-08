class Ebook:
    """This class would represent an ebook which has the typical attributes (title, author, .....)."""

    # This is the constructor for Ebook where it includes their attributes (title, author,...., isbn)
    def __init__(self, title = "", author = "", genre = "", pub_date = "", price = 0.0 , isbn = ""):
        self.__title = title
        self.__author = author
        self._genre = genre
        self._pub_date = pub_date
        self.__price = price
        self.__isbn = isbn

    # Here is a method for ebook, where it gets all book's details.
    def get_details(self):
        return {
            "title": self.__title,
            "author": self.__author,
            "genre": self._genre,
            "publication_date": self._pub_date,
            "price": self.__price,
            "isbn": self.__isbn
        }
        #Note: I am putting them as a dictionary.

    # Getter and Setter (for price)
    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    # A sting method where I want it to return details as a string.
    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Price: {self.__price} AED"
