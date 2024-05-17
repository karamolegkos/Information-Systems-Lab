import datetime
from flask import request
import jwt
from app import server
from app.repository import Repository
from app.model.book import Book
from app.middleware import token_required

rep = Repository.instance()


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
