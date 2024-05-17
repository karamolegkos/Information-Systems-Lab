

from flask import request
from app import server
from app.middleware import token_required
from app.repository import Repository

rep = Repository.instance()


@server.route('/books', methods=['GET'])
def books():
    book_id = request.args.get('id')
    from_index = request.args.get('from')
    to_index = request.args.get('to')
    # Ασκήσεις
    author:str = request.args.get('author')
    title:str = request.args.get('title')
    genre:str = request.args.get('genre')
    comments_min:str = request.args.get('comments_min')
    comments_max:str = request.args.get('comments_max')
    rating_min:str = request.args.get('min')
    rating_max:str = request.args.get('max')
    from_date:str = request.args.get('from_date')
    to_date:str = request.args.get('to_date')
    items_min:str = request.args.get("items_min")
    items_max:str = request.args.get("items_max")
    books = []
    if book_id is not None:
        book = rep.get_book_by_id(book_id)
        return (book.to_dict(), 200) if book else ("Book not found", 404)
    elif from_index is not None and to_index is not None:
        # PAGINATION
        books = rep.get_books(from_index, to_index)
    # TODO Comment
    elif author is not None:
        pass
    elif title is not None:
        pass
    elif genre is not None:
        pass
    elif rating_min is not None and rating_max is not None:
        pass
    elif from_date is not None and to_date is not None:
        pass
    elif items_min is not None  and items_max is not None:
        pass
    elif comments_min is not None and comments_max is not None:
        pass
    else:
        books = rep.get_books()

    if books is None:
        return [], 200
    return list(map(lambda x: x.to_dict(), books)), 200

@server.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.get_json()
    pass

@server.route('/books', methods=['PATCH'])
@token_required
def update_items():
    pass