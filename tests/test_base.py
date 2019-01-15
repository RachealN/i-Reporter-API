import unittest
from  app.views import redflag_view
from app import initialize_app



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

    def tearDown(self):
       self.redflags.clear()
       self.users.clear()
       
        

       
        