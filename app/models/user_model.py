import json
import datetime


users = [] 


class UserModel:

    def __init__(self):
        self.users = users
        

    def add_user(self,args):
        """initialize user's parameters"""
        user = dict(
                user_id = len(users) + 1,
                firstname = args['firstname'],
                lastname = args['lastname'],
                othernames = args['othernames'],
                email = args['email'],
                phonenummber = args['phonenumber'],
                password = args['password'],
                username = args['username'],
                registered = str(datetime.datetime.now()),
                isAdmin = True
            )

        users.append(user)
        return user
           
    def get_all_users(self):
        return self.users
        
    def get_user_by_id(self,userId):
        for user in self.users:
            if user['user_id'] == userId:
                return user
        return None

    


  
