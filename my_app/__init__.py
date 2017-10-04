from flask import Flask
app = Flask(__name__)
from my_app.views import shoppinglist
app.register_blueprint(shoppinglist)
