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
    id = request.args.get('id')
    if id is not None:
        book = db.get_book_by_id(id)
        return (book.to_dict(), 200) if book else ("Book not found", 404)
    else:
        books = db.get_books()
        return books, 200


@server.route('/books', methods=['POST'])
@token_required
def book():
    data = request.get_json()
    if data is None:
        return "Missing parameters"
    if not data.get('title') or not data.get('author') or not data.get('year'):
        return "Missing parameters", 400
    book = Book(data.get('title'), data.get('author'), data.get('year'))
    db.add_book(book)
    return {"message": "CREATED", "data": {"id": book.id}}, 201


@server.route('/books/<id>', methods=['DELETE'])
@token_required
def delete_book(id):
    deleted = db.delete_book(id)  
    return ({"message":"DELETED", "data": {"id": id}}, 200) if deleted else ("Book not found", 404)


@server.route('/books/<id>', methods=['PUT'])
@token_required
def update_book(id):
    data = request.get_json()
    if data is None:
        return "Missing parameters", 400
    if not data.get('title') and not data.get('author') and not data.get('year'):
        return "Missing parameters", 400
    result = db.update_book(id, data)
    return ({"message":"UPDATED", "data": {"id": id}}, 200) if result else ("Book not found", 404)


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

    print(token)
    return ({'message': 'OK' ,'token': token}, 200)
