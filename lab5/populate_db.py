
import pymongo
import json
import os

from app.model.user import User
from app.utils.crypto_utils import encrypt_password


def main():
    # cryptography
    # key = Fernet.generate_key()
    
    # Connection for usage from the Lab
    # client = pymongo.MongoClient("83.212.238.166", 27017)
    client = pymongo.MongoClient("localhost", 27017)
    # Or 
    # client = MongoClient("mongodb://localhost:27017/")
    
    db = client.bookstore
    # Or
    # db = client["bookstore"]

    # Populate books
    with open(os.path.join("assets","books.json"), "r") as books_file:
        books:list[User] = json.load(books_file)
    result = db["books"].insert_many(books)
    print(len(result.inserted_ids), "Books created")

    # Populate users
    with open(os.path.join("assets", "users.json"), "r") as users_file:
        users:list[User] = json.load(users_file)
    for user in users:
        user["password"] = encrypt_password(user["password"])
    result = db["users"].insert_many(users)
    print(len(result.inserted_ids), "Users created")

    # Populate genres
    result = db["genres"].insert_many([
        {"type": 'Fiction'}, 
        {"type":'Historical Fiction'}, 
        {"type": 'Mystery'}, 
        {"type": 'Non-fiction'}, 
        {"type": 'Romance novel'}, 
        {"type": 'Novel'}, 
        {"type": 'Science fiction'}, 
        {"type": 'Short Story'}, 
        {"type": 'Science'}, 
        {"type": 'Fantasy'}]
        )
    print(len(result.inserted_ids), "Genres created")
    



    




if __name__ == "__main__":
    main()
