from flask import abort
from app.data.data import users


class User:
    def __init__(self,**kwargs):
        self.id = kwargs.get("id")
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.othernames = kwargs.get("othernames")
        self.email = kwargs.get("email")
        self.phoneNumber = kwargs.get("phoneNumber")
        self.registered = kwargs.get("registered")
        self.isAdmin = kwargs.get("isAdmin")
    
    def add_user(self, id,firstname,lastname,othernames,email,phoneNumber,registered,isAdmin):
        try:
            user = {
                id:id,
                "firstname":firstname,
                "lastname":lastname,
                "othernames":othernames,
                "email":email,
                "phoneNumber":phoneNumber,
                "registered":registered,
                "isAdmin":isAdmin
            }
            
            users.append(user)
            return user

        except Exception as identifier:
            return identifier

    def get_all_users(self):
        return users