import unittest2 as unittest2
from flask import Flask
from my_app import app
import tempfile
class ShoppingListTest(unittest2.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        self.app=app.test_client()
    def test_if_login_page_works(self):
        rv=self.app.get('/')
        self.assertEqual(rv.status_code,200)
if __name__ =='__main__':
    unittest2.main()