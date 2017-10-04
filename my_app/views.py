from flask import render_template,Blueprint,request,redirect,flash,url_for,session
from my_app import app
shoppinglist=Blueprint('shoppinglist',__name__)
@shoppinglist.route('/',methods=['POST','GET'])
def home():
    return render_template('Login.html')
@shoppinglist.route('/signup',methods=['POST','GET'])
def signUp():
    return render_template('Registration.html')