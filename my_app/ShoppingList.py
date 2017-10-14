class ShoppingList:
    UserShoppingList=[]
    def getlist(self):
        return self.UserShoppingList
    def add(self,name):
        self.UserShoppingList=self.UserShoppingList+[name]
    def rename(self,name,newname):
        for u in self.UserShoppingList:
            if u==name:
                i=self.UserShoppingList.index(u)
                self.UserShoppingList[i]=newname
    def de(self,name):
        self.UserShoppingList.remove(name)
        
