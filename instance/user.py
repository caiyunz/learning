#!/usr/bin/python3
class User():
    def __init__(self,first_name,last_name,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.login_attempts=0

    def increment_login_attempts(self):
        self.login_attempts+=1
        print("User has attempted login:"+str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts=0
        print("User attempted login set to 0!")

    def describe_user(self):
        print("User's name is:"+self.first_name+" "+self.last_name)
        print("User's gender is:"+self.gender)

    def great_user(self):
        print("Hello,welcom to python3 world!")

class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name,gender):
        super().__init__(first_name,last_name,gender)
        self.privilege=Privileges()
    

user1=User('Eric','toms','male')
user1.describe_user()
user1.great_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()

user2=User('Nancy','lee','female')
user2.describe_user()
user2.great_user()

user3=Admin('Toms','jason','male')
user3.privilege.show_privileges()
