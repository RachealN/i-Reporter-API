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
            comment = "bribe",
            createdOn = "Sun, 09 Dec 2018 13:25:47 GMT",
            image = "img",
            incidentType = "red-flag",
            location = "0236556",
            status = "draft",
            user_id = 2,
            video = ["Image","Image"]
           
            )
        self.redflags_empty = []
        self.redflags=[self.redflag,self.redflag]
        
