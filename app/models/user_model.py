import json

            
class IncidentUser:
    Num_of_users = 0
    
    def __init__(self,firstname,lastname,email,password,othernames,phonenumber,
    username,registered,isAdmin,user_id):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.othernames = othernames
        self.phonenumber = phonenumber
        self.registered = registered
        self.isAdmin = isAdmin
        self.user_id = user_id


    def to_json(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "othernames": self.othernames,
            "phonenumber": self.phonenumber,
            "registered": self.registered,
            "isAdmin": self.isAdmin,
            "user_id": self.user_id,
            
        }
class Registration(IncidentUser):
    def create_user_email(self):
        pass

    def create_user_password(self):
        pass


class User(IncidentUser):
    def __init__(self,users = None):
        if users is None:
            self.users = []
        else:
            self.users = users

        
    def add_redflag_user(self,user):
        if user not in self.users:
            return self.users.append(user)

    def get_redflag_users(self,user):
        return self.users
        
    def get_redflag_user_id(self,user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None


   