class User:

    userNum = 0

    def __init__(self,name,password):
        self.name = name
        self.password = password
        User.userNum += 1
        print('a new user object')

    def __del__(self):
        print 'an  %s  object was destroyed '% self.__class__

    def showUser(self):
        print "user name:"+" "+self.name
        print "user pass:" +" "+self.password
        print "there is  %d  users already" % User.userNum

user = User('wang','password')
user.age = 100
print getattr(user,'age')
del user
