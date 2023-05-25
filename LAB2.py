Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template
...  
... app = Flask(__name__)
...  
... class Book:
...     def __init__(self, title, author, genre):
...         self.title = title
...         self.author = author
...         self.genre = genre
...  
... class Bookstore:
...     def __init__(self, name, books):
...         self.name = name
...         self.books = books
...  
... # Создание нескольких книг
... book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
... book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
... book3 = Book("Pride and Prejudice", "Jane Austen", "Classic")
... book4 = Book("1984", "George Orwell", "Dystopian")
... book5 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
...  
... # Создание нескольких книжных магазинов
... bookstore1 = Bookstore("Bookstore A", [book1, book2])
... bookstore2 = Bookstore("Bookstore B", [book3, book4, book5])
...  
... @app.route("/")
... def home():
...     return render_template('index.html', bookstores=[bookstore1, bookstore2])
...  
... @app.route("/book/<title>")
... def book_details(title):
...     # Поиск книги по названию
...     for bookstore in [bookstore1, bookstore2]:
...         for book in bookstore.books:
...             if book.title == title:
...                 return render_template('book.html', book=book)
    return "Книга не найдена."
 
if __name__ == "__main__":
