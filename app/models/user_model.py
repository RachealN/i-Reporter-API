import json
import datetime


users = [] 
         

class UserModel:
    # Num_of_users = 0
    def __init__(self):
        self.users = users
        

    def add_user(self,args):
        
            user = dict(
                user_id = len(users) + 1,
                firstname = args['firstname'],
                lastname = args['lastname'],
                othernames = args['othernames'],
                email = args['email'],
                phonenummber = args['phonenumber'],
                username = args['username'],
                registered = str(datetime.datetime.now()),
                isAdmin = args['isAdmin']

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

    def get_user_by_email(self,email):
        for user in self.users:
            if user['email'] == email:
                return user
        return None


   