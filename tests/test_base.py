import unittest
from flask import Flask,json
from  app.views import redflag_view
from app.models import redflag_model  
from app import initialize_app



class TestBase(unittest.TestCase):
    
    def setUp(self):
        self.app = initialize_app()
        self.client = self.app.test_client(self)
        # self.incident=dict(
            
        #     createdOn = "1-1-2018",
        #     createdBy = "Racheal",
        #     type = "red-flag",
        #     location = 'Kampala',
        #     status = "none",
        #     comment = "fight corruption"
        #     )
        # self.incidents_empty = []
        # self.incidents=[self.incident,self.incident]

        
