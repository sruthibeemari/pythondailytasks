class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def displayBook(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Price: ",self.price)

class EBook(Book):
    def __init__(self, title, author, price,fileSize):
        super().__init__(title, author, price)
        self.fileSize=fileSize


    def displayEbook(self):
        self.displayBook()
        print("File Size: ",self.fileSize,"MB")


ebook1=EBook("Python","John",500,5)
ebook1.displayEbook()
