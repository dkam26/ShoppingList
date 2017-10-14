from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY']='Random Key'
from my_app.views import shoppinglist
app.register_blueprint(shoppinglist)
