class User:
    userInfo=dict()
    def signup(self,user,surname,Firstname,email,Password):
        self.userInfo={'username':user,'surname':surname,'Firstname':Firstname,'email':email,'Password':Password}
        return self.userInfo
    def login(self,user,password):
        if self.userInfo['username'] == user and self.userInfo['Password'] == password:
            return 'Success'
        else:
            return 'Failed'
    def logout(self):
        pass
    def EditInfo(self):
        pass
    def deleteAccount(self):
        pass
    
