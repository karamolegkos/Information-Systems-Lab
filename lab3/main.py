
import os

from app import server

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
server.config['SECRET_KEY'] = SECRET_KEY

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)
