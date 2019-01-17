import unittest
from  app.views import redflag_view
from app import initialize_app
import json



class TestBase(unittest.TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""

        self.app = initialize_app()
        self.client = self.app.test_client(self) 
    
        
        self.redflag=dict(
            comment = "corruption",
            createdon = "Sun, 06 Jan 2019 22:03:35 GMT",
            image = "https://postimage/image1.jng",
            incidentType = "redflag",
            location = "234334.56443",
            status = "draft",
            createdBy = 1,
            video = "https://postvideo/Video5.jng"
           
            )
        self.redflags_empty = []
        self.redflags=[self.redflag,self.redflag]
        

        self.user = dict(
            firstname = "okello",
            lastname = "opio",
            othernames = "heloo",
            email = "odetah@gmail.com",
            username = "Ahabwe",
            password  = "12345",
            phonenumber = "0786576572"
        )  
        self.users_empty = []
        self.users=[self.user,self.user]

   
        self.credential = dict(
            email = "odetah@gmail.com",
            password = "12345"
        )
        self.credentials_empty = []
        self.credentials=[self.credential,self.credential]

    # def register_user(self):
    #     newuser={
    #             "firstname":"okello",
    #             "lastname":"opio",
    #             "othernames":"heloo",
    #             "email":"odetah@gmail.com",
    #             "username":"Ahabwe",
    #             "password":"12345",
    #             "phonenumber":"0786576572"


    #                 }
    #     response = self.client.post('/api/v1/register',
    #             content_type='application/json',
    #             data=json.dumps(newuser))
        

    # def login_user(self):
    #     self.register_user()

    #     credentials={
    #         "email":"odetah@gmail.com",
    #         "password":"12345"
    #         }
    #     response = self.client.post('/api/v1/login',
    #     content_type='application/json',
    #     data=json.dumps(credentials))

    #     token=json.loads(response.data.decode())
    #     token=token.get('Token')[0]

    # def access_token(self,email='odetah@gmail.com',password='12345'):
        
    #     response = self.client.get()
    #     return json.loads(response.data.decode())['token']

    
    # def create_redflag(self):
    #     self.login_user()
        
    #     token=json.loads(response.data.decode())
    #     token=token.get('Token')[0]

    #     redflags = []
    #     response = self.client.post('/api/v1/red-flags',
    #     content_type='application/json',headers=dict(Authorization='Bearer '+token),
    #     data=json.dumps(dict(
    #         comment = "corruption",
    #         createdOn = "Sun, 06 Jan 2019 22:03:35 GMT",
    #         image = "https://postimage/image1.jng",
    #         incidentType = "redflag",
    #         location = "6554.7898",
    #         status = "draft",
    #         createdBy = 1,
    #         video = "https://postvideo/Video5.jng"
    #     )))
    #     redflags.append(dict)
        
    # def get_token(self,  email = "odetah@gmail.com", password="12345"):
        
    #     response = self.login_user(email, password)
    #     return token=json.loads(response.data.decode())


    

    def tearDown(self):
       self.redflags.clear()
       self.users.clear()


    

    