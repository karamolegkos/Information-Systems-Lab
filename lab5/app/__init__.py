from flask import Flask

server = Flask(__name__)

from app import routes, routes2

