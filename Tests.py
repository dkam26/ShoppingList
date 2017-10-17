import unittest2 as unittest2
from flask import Flask
from my_app import app
import tempfile
from my_app.User import User
from my_app.ShoppingList import ShoppingList
from my_app.Product import Product
Shopper=User()
Shopper_list=ShoppingList()
Shopper_Product=Product()
userInfo={'username':'dkam26','surname':'kamara','Firstname':'deo','email':'dk@gmail.com','Password':'123'}
username='dkam26'
surname='kamara'
Firstname='deo'
email='dk@gmail.com'
Password='123'
class ShoppingListTest(unittest2.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        self.app=app.test_client()
    def test_if_signup_works(self):
        self.assertEqual(userInfo,Shopper.signup(username,surname,Firstname,email,Password))
    def test_if_login_succeeds(self):
        username='dkam26'
        surname='kamara'
        Firstname='deo'
        email='dk@gmail.com'
        Password='123'
        Shopper.signup(username,surname,Firstname,email,Password)
        self.assertEqual('Success',Shopper.login(username,Password))
    def test_if_login_has_wrong_creditinals(self):
        username='dkam26'
        surname='kamara'
        Firstname='deo'
        email='dk@gmail.com'
        Password='123'
        us='dkam'
        pa='1'
        Shopper.signup(username,surname,Firstname,email,Password)
        self.assertEqual('Failed',Shopper.login(us,pa))
    def test_if_app_returns__lists_of_shoppinglist(self):
        shoppping_list=Shopper_list.UserShoppingList
        self.assertEqual(shoppping_list,Shopper_list.getlist())
    def test_if_app_adds_shoppinglist_elements(self):
        u=[]
        NewElement='trousers'
        newlist=u+[NewElement]
        self.assertEqual(newlist,Shopper_list.add(NewElement))
    def test_if_app_renames_shoppinglist_elements(self):
        testshopperlist=['trousers']
        i=testshopperlist.index('trousers')
        testshopperlist[i]='shirts'
        self.assertEqual(testshopperlist,Shopper_list.rename('trousers','shirts')) 
    
    def test_if_app_returns_products_of_a_list(self):
        Shopper_Product.products={'trousers':{}}
        testshopperproducts=Shopper_Product.products['trousers']
        self.assertEqual(testshopperproducts,Shopper_Product.getproducts('trousers'))
    def test_if_app_add_new_products(self):
        testshopperdictionary={}
        x={'trousers':{'khaki pants':[2,45000]}}
        testproduct=Shopper_Product.addlis('trousers')
        self.assertEqual(x['trousers'],Shopper_Product.addproducts('trousers','khaki pants',2,45000))
        
    

        
    


if __name__ =='__main__':
    unittest2.main()