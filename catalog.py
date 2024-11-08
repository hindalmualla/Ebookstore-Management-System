#just calling back to the Ebook file (attributes to be added here).
from ebook import Ebook

class Catalog:
    """This class would represent the catalog which has the ebooks."""

    #constructor for ebook
    def __init__(self):
        self._ebook = []

    #method to add books
    def add_ebook(self, ebook):
        self._ebook.append(ebook)

    #method to remove books
    def remove_ebook(self, isbn):
        self._ebook = [book for book in self._ebook if book.get_details()["isbn"] != isbn]

    # method to scour the list to find all books
    def find_ebook_title(self, title):
        #Here, I am using the for loop to go through titles
        for ebook in self._ebook:
            if ebook.get_details()["title"] == title: #if it matches the ebook title
                return ebook #returns the first matching ebook
        return None #returns if it does not find

    #It lists of all the books in the catalog
    def list_books_all(self):
        result = [] # an empty list to store ebooks
        #using for loop to iterate over each ebook in the ebook list
        for ebook in self._ebook:
            result.append(str(ebook)) #convert into object, and append it to result list
        return result #returns all ebook as string

    #using str method, this would return as a string for all ythe books in the catalog.
    def __str__(self):
        #header
        catalog_str = "Catalog:\n"
        #lists of all the ebooks as strings
        catalog_str += "\n".join(self.list_books_all()) #using join to combine with newlines
        return catalog_str