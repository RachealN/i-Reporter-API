import unittest
import json
from app import initialize_app
from .test_base import TestBase 
from  app.views import users_view


class AuthTestCase(TestBase):
    """Test case for the Authentication Blueprint."""
    
    def test_register_user(self):
        users = []
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(dict(
                self.user
        )))
        users.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(len(users),2)
        self.assertNotEqual("user with id is not found",str(response.data))

    
    def test_login_user(self):
        """Test API can login a user"""

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

       
    
    
    def test_get_users(self):
        """Test API can get all users"""

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
        
        
        response = self.client.get('/api/v1/users',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.users_empty))
        self.assertEqual(len(self.users_empty),0)
    
    
    def test_get_single_user_by_id(self):
        """Test API can get user by id"""
        
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
        
        
        response = self.client.get('/api/v1/users/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.user))
        self.assertEqual(response.status_code,200)
        self.assertTrue(self.user,response.data)
        self.assertNotEqual("user with that id is not found",str(response.data))
    

       

    def test_get_users_empty_list(self):
        """Test API cannot get empty list of users"""
        
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

        response = self.client.get('/api/v1/users',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.users_empty))
        self.assertEqual(len(self.users_empty),0)

    
    def test_delete_user(self):
        """Test API can delete a user"""
        
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
        
        response=self.client.delete('/api/v1/users/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(self.redflags),1)
        self.assertNotEqual("user with that id doesnt exist",str(response.data))
    
    def test_delete_redflag_doesnt_exist(self):
        """Test API cannot delete user that doesnot exist"""
        
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



        response=self.client.delete('/api/v1/users/2',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        data=json.dumps(self.users_empty)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.users_empty),0)
        self.assertNotEqual("user with that id doesnt exist",str(response.data))
    
    
    def test_non_registered_user_login(self):
        """Test non registered users cannnot login."""

        self.user
        response = self.client.post('/api/v1/register',
        content_type='application/json',
        data=json.dumps(self.user))

        not_a_user = {
            'email':'not_a_user@hmail.com',
            'password':'none'

        }

        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(not_a_user))
        
        self.assertNotEqual("Invalid email or password, Please try again",str(response.data))
        self.assertNotEqual("Not registered,please register first before logging in",str(response.data))
    

    

    