class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
title = input("enter the title:")
author = input("enter the author:")
price = float(input("enter the price:"))
book = Book(title,author,price)
print("Title:",book.title)
print("Author:",book.author)
print("Price:",book.price)