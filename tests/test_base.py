import unittest
from flask import Flask,json
from  app.views import redflag_view
# from app.models import redflag_model  
from app import initialize_app



class TestBase(unittest.TestCase):
    
    def setUp(self):
        self.app = initialize_app()
        self.client = self.app.test_client(self)
        self.redflag=dict(
            comment = "corruption",
            createdon = "Sun, 06 Jan 2019 22:03:35 GMT",
            image = "img",
            incidentType = "redflag",
            location = "video",
            status = "draft",
            createdBy = 1,
            video = "dsfdghgh"
           
            )
        self.redflags_empty = []
        self.redflags=[self.redflag,self.redflag]
        

   
        self.user = dict(
            id = 1,
            firstname = "Namaara",
            lastname = "Racheal",
            othernames = "Rapheal",
            email = "recheal@gmail.com",
            phonenumber = "0786576572",
            username = "RachealN",
            registered = "2019-01-06 21:11:12.985062",
            isAdmin = "True"
            
        )  
        self.users_empty = []
        self.users=[self.user,self.user]
        
        
    

        self.user_data = {
            'email':'racheal@gmail.com',
            'password':'hello'
        }
        self.users = [self.user_data,self.user_data]

    
        