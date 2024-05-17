from typing import Optional
import uuid


class Book:
    def __init__(self,
                 id: Optional[str],
                 title: str,
                 author: str,
                 year: int,
                 summary: str,
                 items: int,
                 price: float,
                 genre: str,
                 cover: Optional[str],
                 rating: Optional[float],
                 comments: Optional[str]
                 ):
        self.id: str = id if id is not None else str(uuid.uuid4())
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.summary: str = summary
        self.items: int = items
        self.price: float = price
        self.genre: str = genre
        self.cover: Optional[str] = cover
        self.rating: Optional[int] = rating
        self.comments: Optional[str] = comments

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.id} - {self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Books('{self.id}', '{self.title}', '{self.author}', {self.year})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "rating": self.rating,
            "comments": self.comments,
            "cover": self.cover,
            "genre": self.genre,
            "summary": self.summary,
            "items": self.items,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("id"),
            data.get("title"),
            data.get("author"),
            data.get("year"),
            data.get("summary"),
            data.get("items"),
            data.get("price"),
            data.get("genre"),
            data.get("cover"),
            data.get("rating"),
            data.get("comments")
        )
            
        

