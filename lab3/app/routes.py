import datetime
from flask import request
import jwt
from app import server
from app.repository import Repository
from app.model.books import Book
from app.middleware import token_required

db = Repository()

# Routes
# Get all the books
@server.route('/books/all', methods=['GET'])
# @token_required # Remove to allow access only with Bearer Token
def get_all_books():
    books = db.get_books()
    return books, 200


# Get a book by id
@server.route('/books', methods=['GET'])
def get_book():
    # The endpoint should be something like the following: http://localhost:5000/books?id=95c57eed-6c06-4ed5-a44b-00073063628b
    # id = request.args.get('id')
    # Check repository.py for the methods of the db object
    # Check the model/books.py for the methods of a book object
    # Υλοποιήστε τον κώδικα σας
    pass


# Add a book to the library
@server.route('/books', methods=['POST'])
def add_book():
    # data = request.get_json()
    # Υλοποιήστε τον κώδικα σας
    pass


# Delete a book from the library
@server.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    # The endpoint should be something like the following: http://localhost:5000/books/95c57eed-6c06-4ed5-a44b-00073063628b
    # The id parameter is being gathered by the function delete_book(id)
    # Υλοποιήστε τον κώδικα σας
    pass


# Update a book in the library. This function is using token authentication
@server.route('/books/<id>', methods=['PUT'])
def update_book(id):
    # data = request.get_json()
    # Υλοποιήστε τον κώδικα σας
    pass


@server.route('/token', methods=['POST'])
def get_token():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return "Missing parameters", 400
    
    username = auth.get('username')
    password = auth.get('password')

    print(auth)

    if username != 'admin' or password != 'admin':
        return "Invalid credentials", 401
    # Generate token    
    token = jwt.encode(
        {
            'name': 'The Bookstore API',
            'role': 'administrator',
            'username': username, 
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=30),
        },
        server.config['SECRET_KEY'],
        algorithm='HS256'
    )
    
    return ({'message': 'OK' ,'token': token}, 200)
