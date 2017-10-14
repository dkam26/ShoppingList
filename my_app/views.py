from flask import render_template,Blueprint,request,redirect,flash,url_for,session
from my_app import app
from my_app.User import User
from my_app.ShoppingList import ShoppingList
from my_app.Product import Product
NewUser=User()
product=Product()
UserList=ShoppingList()
shoppinglist=Blueprint('shoppinglist',__name__)
@shoppinglist.route('/')
def home():
    return redirect(url_for('shoppinglist.login'))
@shoppinglist.route('/login/',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form.get('UserName')
        userpass=request.form.get('LoginPassword') 
        result=NewUser.login(user,userpass)
        if result == 'Success':
            return redirect(url_for('shoppinglist.view'))
        else:
            return redirect(url_for('shoppinglist.login'))

        
    return render_template('Login.html')
@shoppinglist.route('/signup',methods=['POST','GET'])
def signUp():
    
    if request.method=='POST':
        user=request.form.get('UserName')
        Surname=request.form.get('SecondName')
        Firstname=request.form.get('FirstName')
        email=request.form.get('Email')
        Password=request.form.get('Password')
        userInfo=NewUser.signup(user,Surname,Firstname,email,Password)
        return redirect(url_for('shoppinglist.login'))
    return render_template('Registration.html')
@shoppinglist.route('/list')
def view():
    UserShoppingList=UserList.getlist()
    return render_template('ShoppingLists.html',shoppinglist=UserShoppingList)
@shoppinglist.route('/addlist',methods=['POST','GET'])
def addShoppinglist():
    if request.method=='POST':
        name=request.form.get('shoppinglistname')
        UserList.add(name)
        return redirect(url_for('shoppinglist.view'))
    return render_template('AddList.html')
@shoppinglist.route('/rename/<name>',methods=['POST','GET'])
def updateList(name):
    if request.method=='POST':
        newname=request.form.get('newname')
        UserList.rename(name,newname)
        product.renamelist(name,newname)
        
        return redirect(url_for('shoppinglist.view'))

    return render_template('UpdateList.html',name=name)
@shoppinglist.route('/delete/<name>')
def deleteList(name):
    UserList.de(name)
    product.deletelist(name)
    return redirect(url_for('shoppinglist.view'))
@shoppinglist.route('/products',methods=['POST','GET'])
def Products():
    if request.method=='POST':
        name=request.form.get('shoppinglist_name')
        if name in product.products:
            p=product.getproducts(name)
        else:
            product.addlis(name)
            p=product.getproducts(name)
        return render_template('ShoppingList.html',p=p,name=name)
@shoppinglist.route('/addItem/',methods=['POST','GET'])
def addItem():
    if request.method=='POST':
        shoppinglist_name=request.form.get('shoppinglist_name')
    return redirect(url_for('shoppinglist.addingItem',shoppinglist_name=shoppinglist_name))
@shoppinglist.route('/Item/<shoppinglist_name>',methods=['POST','GET'])
def addingItem(shoppinglist_name):
    shoppinglist_name=shoppinglist_name
    if request.method=='POST':
        produc=request.form.get('product')
        Quantity=request.form.get('Quantity')
        AmountSpent=request.form.get('AmountSpent')
        product.addproducts(shoppinglist_name,produc,Quantity,AmountSpent)
        p=product.getproducts(shoppinglist_name)
        return render_template('ShoppingList.html',p=p,name=shoppinglist_name)
    return render_template('AddProduct.html',shoppinglist_name=shoppinglist_name)
@shoppinglist.route('/updateItem/',methods=['POST','GET'])
def updateItem():
    if request.method=='POST':
        shoppinglist_name=request.form.get('shoppinglistname')
        name=request.form.get('name')
        Quantity=request.form.get('Quantity')
        Amountspent=request.form.get('Amountspent')
        return redirect(url_for('shoppinglist.updatingItem',shoppinglist_name=shoppinglist_name,name=name,Quantity=Quantity,Amountspent=Amountspent))
@shoppinglist.route('/updatingItem/<shoppinglist_name>/<name>/<Quantity>/<Amountspent>',methods=['GET','POST'])
def updatingItem(shoppinglist_name,name,Quantity,Amountspent):
    shoppinglist_name=shoppinglist_name
    name=name
    Quantity=Quantity
    Amountspent=Amountspent
    if request.method=='POST':
        newQuantity=request.form.get('Quantity')
        newAmount=request.form.get('AmountSpent')
        product.updateItem(shoppinglist_name,name,newQuantity,newAmount)
        p=product.getproducts(shoppinglist_name)
        return render_template('ShoppingList.html',p=p,name=shoppinglist_name)
    return render_template('UpdateItem.html',shoppinglist_name=shoppinglist_name,name=name,Quantity=Quantity,Amountspent=Amountspent)

@shoppinglist.route('/delete',methods=['GET','POST'])
def deleteItem():
    if request.method=='POST':
        shoppinglist_name=request.form.get('shoppinglistname')
        name=request.form.get('name')
        p=product.deleteItem(shoppinglist_name,name)
        return render_template('ShoppingList.html',p=p,name=shoppinglist_name)