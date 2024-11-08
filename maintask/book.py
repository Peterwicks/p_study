# .Create a class Book with attributes like title, author, and year.
# Add a method that returns a description of the book.
# Create an object of Book and print out the description.
class Book():
    def __init__(self, tittle, author, year):
        self.tittle = tittle
        self.author=author
        self.year= year
    def book_description(self):
        return f'The book {self.tittle} written by {self.author} was published in the year {self.year}'
Book1=Book('River and The Source', 'Margret A. Ogola', '2004') 
print(Book1.book_description())
