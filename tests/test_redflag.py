import unittest
from  app.views import redflag_view
from .test_base import TestBase  
from app import initialize_app
import json


class TestRedFlag(TestBase):
    """This class represents the redflag test case"""
    
    
    def test_index(self):
        response = self.client.get('/api/v1/')
        data = response.data.decode()
        message ={"message": "Welcome to I-Reporter", "status": 200}
        self.assertEqual(json.loads(data), message)
        

    def test_created_redflag(self):
        """Test API can create a redflag(POST request)"""

        
        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

    
        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token = json.loads(response.data.decode()),
        token = token.get('Token')[0]
       
        

        redflags = []
        response = self.client.post('/api/v1/red-flags',
        content_type='application/json',headers=dict(Authorization= 'Bearer' + token),
        data=json.dumps(dict(
            self.redflag
        )))
        
        redflags.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("Redflag not created",str(response.data))
        
    
    def test_get_redflags(self):
        """Test API can get redflags (GET request)."""

        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))


        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        response = self.client.get('/api/v1/red-flags',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.redflags_empty))
        self.assertEqual(len(self.redflags_empty),0)
        self.assertNotEqual("Redflag not found",str(response.data))
        
    
    
    def test_get_redflags_empty_list(self):
        
        response = self.client.get('/api/v1/red-flags',
        content_type='application/json',
        data=json.dumps(self.redflags_empty))
        self.assertEqual(len(self.redflags_empty),0)

    def test_get_single_redflag_by_id(self):
        """Test API can get a single redflag by using it's id."""

        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        
        response = self.client.get('/api/v1/red-flags/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.redflag))
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.redflag,response.data)
        self.assertNotEqual("Redflag with that id is not found",str(response.data))
        

    def test_edit_redflag_location(self):
        """Test API can edit an existing location. (PATCH request)"""
        
        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        response = self.client.patch('/api/v1/red-flags/1/location',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data = json.dumps(dict(
            location = "86574.7686")))

        redflags = []
        response = self.client.post('/api/v1/red-flags',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(dict(
            self.redflag
        )))
        redflags.append(dict)
        

        self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(self.redflag,response.data)
        self.assertNotEqual("red-flag location with that id not found",str(response.data))
        
    
       
    def test_edit_redflag_comment(self):
        """Test API can edit an existing comment. (PATCH request)"""

        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]

        redflags = []
        response = self.client.post('/api/v1/red-flags',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(dict(
            self.redflag
        )))
        redflags.append(dict)
        
        response = self.client.patch('/api/v1/red-flags/1/comment',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data = json.dumps(dict(
            comment = "rape")))
        
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.redflag,response.data)
        self.assertIn("",str(response.data))
        self.assertNotEqual("red-flag comment with that id not found",str(response.data))
        
        

    def test_delete_redflag(self):
        """Test API can delete an existing redflag. (DELETE request)."""
        
        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        response=self.client.delete('/api/v1/red-flags/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(self.redflags),1)
        self.assertIn("Redflag with that id doesnot exist",str(response.data))


    def test_delete_redflag_doesnt_exist(self):
        """Test API can delete non_existing redflag. (DELETE request)."""
        
        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

        self.credential
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(self.credential))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]



        response=self.client.delete('/api/v1/red-flags/2',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        data=json.dumps(self.redflags_empty)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.redflags_empty),0)
       
        

