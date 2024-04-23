import datetime
from flask import request
import jwt
from app import server
from app.repository import Repository
from app.model.books import Book
from app.middleware import token_required

db = Repository()

# Routes    
@server.route('/books', methods=['GET'])
def books():
    # id = request.args.get('id')
    # Υλοποιήστε τον κώδικα σας
    pass


@server.route('/books', methods=['POST'])
def book():
    # data = request.get_json()
    # Υλοποιήστε τον κώδικα σας
    pass


@server.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    pass


@server.route('/books/<id>', methods=['PUT'])
@token_required
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
