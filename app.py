from flask import Flask
from extensions import api , db
from resources import ns

def create_app():
    app = Flask(__name__)
    api.add_namespace(ns)
    return app
