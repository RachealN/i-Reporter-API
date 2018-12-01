import unittest
from  app.views import redflag_view
from app.models import redflag_model
from .test_base import TestBase  
from app import initialize_app
from app.data.data import redflags
import json


class TestRedFlag(TestBase):
    def test_index(self):
        response = self.client.get('/api/v1/')
        data = response.data.decode()
        message ={"message": "Welcome to I-Reporter", "status": 200}
        self.assertEqual(json.loads(data), message)
        
    def test_created_redflag(self):
        new_redflag = {
        "createdBy":"Racheal",
        "incidentType":"redflag",
        "location":"0236556",
        "status":"resolved",
        "image":"img",
        "video":"image",
        "comment":"corruption"

        }
        response = self.client.post('/api/v1/red-flags', content_type='application/json',data=json.dumps(new_redflag))
        data =response.data.decode()
        message = {
                "data": [
                    {
                        "comment": "corruption",
                        "createdBy": "Racheal",
                        "createdOn": "Fri, 30 Nov 2018 20:03:53 GMT",
                        "id": 2,
                        "image": "img",
                        "incidentType": "redflag",
                        "location": "0236556",
                        "status": "resolved",
                        "video": "image"
                    }
                ],
                "message": "Redflag created succesfully",
                "status": 201
            }
        self.assertEqual(json.loads(data),message) 
        
        

    def test_get_single_redflag_by_id(self):
        pass

    def test_edit_redflag_location(self):
        pass

    def test_edit_redflag_comment(self):
        pass

    def test_delete_redflag(self):
        pass
        

