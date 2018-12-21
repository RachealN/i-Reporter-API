import unittest
from  app.views import redflag_view
from .test_base import TestBase  
from app import initialize_app
import json


class TestRedFlag(TestBase):
    def test_index(self):
        response = self.client.get('/api/v1/')
        data = response.data.decode()
        message ={"message": "Welcome to I-Reporter", "status": 200}
        self.assertEqual(json.loads(data), message)
        

    def test_created_redflag(self):
        redflags = []
        response = self.client.post('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(dict(
            comment = "bribe",
            createdOn = "Sun, 09 Dec 2018 13:25:47 GMT",
            image = "img",
            incidentType = "red-flag",
            location = "0236556",
            status = "draft",
            user_id = 2,
            video = ["Image","Image"]
        )))
        redflags.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("Redflag with id is not found",str(response.data))
    def test_get_redflags(self):
        response = self.client.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.redflags_empty))
        self.assertEqual(len(self.redflags_empty),0)
    
    def test_get_redflags_empty_list(self):
        response = self.client.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.redflags_empty))
        self.assertEqual(len(self.redflags_empty),0)

    def test_get_single_redflag_by_id(self):
        response = self.client.get('/api/v1/red-flags/2',data=json.dumps(self.redflag))
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.redflag,response.data)

    def test_edit_redflag_location(self):
        
        response = self.client.patch('/api/v1/red-flags/<int:user_id>/location',
        data = json.dumps(dict(
            location = "bribe")))
        
        # self.assertEqual(response.status_code,200)
        self.assertTrue(self.redflag,response.data)
        self.assertIn("",str(response.data))
        self.assertNotEqual("red-flag location with that id not found",str(response.data))

    def test_edit_redflag_comment(self):
        response = self.client.patch('/api/v1/red-flags/<int:user_id>/comment',
        data = json.dumps(dict(
            location = "muk")))
        
        # self.assertEqual(response.status_code,200)
        self.assertTrue(self.redflag,response.data)
        self.assertIn("",str(response.data))
        self.assertNotEqual("red-flag comment with that id not found",str(response.data))
        

    def test_delete_redflag(self):
        pass
        # response=self.client.delete('/api/v1/red-flags/1',
        # content_type='application/json',)
        # self.assertEqual(response.status_code,200)
        # self.assertTrue(len(self.redflags),1)
        # self.assertIn("Redflag has been deleted succesfully",str(response.data))


    def test_delete_redflag_doesnt_exist(self):
        response=self.client.delete('/api/v1/red-flags/2',
        content_type='application/json',
        data=json.dumps(self.redflags_empty))
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.redflags_empty),0)
        self.assertIn("Redflag with that user_id doesnot exist",str(response.data))
       
        

