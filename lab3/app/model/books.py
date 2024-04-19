import uuid

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.id = str(uuid.uuid4())

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
        }
    
    def from_dict(self, data):
        self.id = data.get("id") if data.get("id") is not None else self.id
        self.title = data.get("title") if data.get("title") is not None else self.title
        self.author = data.get("author") if data.get("author") is not None else self.author
        self.year = data.get("year") if data.get("year") is not None else self.year
