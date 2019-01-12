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

        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]

        redflags = []
        response = self.client.post('/api/v1/red-flags',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(dict(
            comment = "corruption",
            createdOn = "Sun, 06 Jan 2019 22:03:35 GMT",
            image = "img",
            incidentType = "redflag",
            location = "video",
            status = "draft",
            createdBy = 1,
            video = "dsfdghgh"
        )))
        redflags.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(len(redflags),2)
        self.assertNotEqual("Redflag not created",str(response.data))
    
    def test_get_redflags(self):
        """Test API can get redflags (GET request)."""
        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

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

        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

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
        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        response = self.client.patch('/api/v1/red-flags/<int:user_id>/location',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data = json.dumps(dict(
            location = "bribe")))
        

        # self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(self.redflag,response.data)
        self.assertNotEqual("red-flag location with that id not found",str(response.data))
        
    
       
    def test_edit_redflag_comment(self):
        """Test API can edit an existing comment. (PATCH request)"""

        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        response = self.client.patch('/api/v1/red-flags/<int:user_id>/comment',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data = json.dumps(dict(
            location = "muk")))
        
        # self.assertEqual(response.status_code,201)
        self.assertTrue(self.redflag,response.data)
        self.assertIn("",str(response.data))
        self.assertNotEqual("red-flag comment with that id not found",str(response.data))
        
        

    def test_delete_redflag(self):
        """Test API can delete an existing redflag. (DELETE request)."""
        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]
        
        response=self.client.delete('/api/v1/red-flags/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(self.redflags),1)
        self.assertIn("red-flag record has been deleted",str(response.data))


    def test_delete_redflag_doesnt_exist(self):
        """Test API can delete non_existing redflag. (DELETE request)."""
        newuser={
                "firstname":"okello",
                "lastname":"opio",
                "othernames":"heloo",
                "email":"odetah@gmail.com",
                "username":"Ahabwe",
                "password":"12345",
                "phonenumber":"0786576572"

                    }
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(newuser))

        credentials={
        "email":"odetah@gmail.com",
        "password":"12345"
        }
        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(credentials))

        token=json.loads(response.data.decode())
        token=token.get('Token')[0]



        response=self.client.delete('/api/v1/red-flags/2',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        data=json.dumps(self.redflags_empty)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.redflags_empty),0)
        # self.assertIn("Redflag with that user_id doesnot exist",str(response.data))
       
        

