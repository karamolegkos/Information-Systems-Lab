
from typing import List
from app.model.books import Book

class Repository:
    def __init__(self) -> None:
        self._add_some_books()
        
    def _add_some_books(self):
        self.books:List[Book] = [Book(author= "J.K. Rowling", title= "Harry Potter and the Philosopher's Stone", year=1997),
                                 Book(author= "J.K. Rowling", title= "Harry Potter and the Chamber of Secrets", year=1998),
                                 Book(author="Agatha Christie", title= "Murder on the Orient Express", year=1934),
                                 Book(author="Jule Verne", title= "Journey to the Center of the Earth", year=1865)
                                 ]
        
    def _find_book_by_id(self, id:str) -> Book | None:
        books = [book for book in self.books if book.id == id]
        if len(books) == 0:
            return None
        return books[0]

    def add_book(self, book:Book) -> None:
        self.books.append(book)

    def get_books(self) -> list[Book]:
        return list(map(lambda x: x.to_dict(),self.books))
    
    def get_book_by_id(self, id:str) -> Book | None:
        book = self._find_book_by_id(id)
        if book is not None:
            return book
        return None

    def update_book(self, id:str, data)-> bool:
        book = self._find_book_by_id(id)
        if book is not None:
            book.from_dict(data)
            return True
        return False
        
    def delete_book(self, id:str) -> bool:
        book = self._find_book_by_id(id)
        if book is not None:
            self.books.remove(book)
            return True
        return False
