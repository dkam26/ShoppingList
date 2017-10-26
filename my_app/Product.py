class Product:
    products={}
    def getproducts(self,name):
        return self.products[name]
        
    def addproducts(self,shoppinglist_name,product,Quantity,AmountSpent):
        x={product:[Quantity,AmountSpent]}
        self.products[shoppinglist_name].update(x)
        return self.products[shoppinglist_name]
    def addlis(self,name):
        y={name:{}}
        self.products.update(y)
        return self.products
    def renamelist(self,name,newname):
        if name in self.products:
            x=self.products[name]
        self.products.pop(name)
        y={newname:x}
        self.products.update(y)
        return self.products
    def deletelist(self,name):
        self.products.pop(name)
    def updateItem(self,shoppinglist_name,name,newQuantity,newAmount):
        if shoppinglist_name in self.products:
            self.products[shoppinglist_name][name]=[newQuantity,newAmount]
        return self.products
    def deleteItem(self,shoppinglist_name,name):
        if shoppinglist_name in self.products:
            self.products[shoppinglist_name].pop(name)
        
        return self.products
