class User:
    name = ''
    email = ''
    password = ''
    login = False
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    def login(self):

        email = input("Enter email: ")
        password = input("Enter password: ")

        if email == self.email and password == self.password:
            User.login = True
            print("Login successful!")
        else:
            User.login = False
            print("Login Failed!")

    def logout(self):

        User.login = False
        print("Logged Out!")

    def isLoggedIn(self):
        if User.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedIn():
            print(self.name,"\n",self.email)
        else:
            print("User is not logged in!")

# user1 = User()
self.__init__(self,"Dip Jit Baroi"",dipjitbaroiofficial@gmail.com",1234)
# user1.name = "Dip Jit Baroi"
# user1.email = "dipjitbaroiofficial@gmail.com"
# user1.password = 1234


user1.login()
# print(user1.login)

user1.profile()


hello = input()

# login(User)
# print(User.login)
# def check_return():
#     num1=2
#     num2=4
#     sum=num1+num2
#     print('inside', sum)
#     return sum
# check_return()
# # print('outside', check_return())
# def multi():
#     num3=6
#     value=num3*check_return()
#     print(value)
# multi()