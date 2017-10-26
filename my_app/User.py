class User:
    userInfo={'username':None,'surname':None,'Firstname':None,'email':None,'Password':None}
    def signup(self,user,surname,Firstname,email,Password):
        self.userInfo={'username':user,'surname':surname,'Firstname':Firstname,'email':email,'Password':Password}
        return self.userInfo
    def login(self,user,password):
        if self.userInfo['username'] == user and self.userInfo['Password'] == password:
            return 'Success'
        else:
            return 'Failed'
    
    
    
