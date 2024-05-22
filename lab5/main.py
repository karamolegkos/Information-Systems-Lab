
import os

from app import server

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
server.config['SECRET_KEY'] = SECRET_KEY

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)


# import pymongo


# def main():
#     # cryptography
#     # key = Fernet.generate_key()
    
    
#     # Connection for usage from the Lab
#     # client = pymongo.MongoClient("83.212.238.166", 27017)
#     client = pymongo.MongoClient("localhost", 27017)
#     # Or 
#     # client = MongoClient("mongodb://localhost:27017/")
#     print(client.list_database_names())
    
#     db = client.bookstore
#     # Or
#     # db = client["bookstore"]
#     print(db.list_collection_names())

#     # Add document in a collection
#     # book = db.books.insert_one({
#     #     "title": "test"
#     # })
#     # print(book.inserted_id)

#     # Query documents
#     result = db.books.find()
#     for r in result:
#         print(r["_id"])

    




# if __name__ == "__main__":
#     main()
