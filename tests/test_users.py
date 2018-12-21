import unittest
import json
from app import initialize_app
from .test_base import TestBase 
from  app.views import users_view


class AuthTestCase(TestBase):
    """Test case for the Authentication Blueprint."""
    
    
    def test_registration(self):
        """Test user registration works correctly."""
        response = self.client.post('/api/v1/register', content_type ='application/json',
        data=self.user_reg)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], "user created but not authenticated, please login first.")
        self.assertEqual(response.status_code,201)
        self.assertTrue(response['content_type'], "application/json")
    
    
    
    def test_already_registered_user(self):
        """Test that a user cannot be registered twice."""
        response = self.client.post('/api/v1/register', content_type='application/json',
        data=self.user_reg)
        self.assertEqual(response.status_code,201)
        self.assertTrue(response['content_type'], "application/json")

        second_response = self.client.post('/api/v1/register',content_type='application/json',
       data=self.user_reg )
        self.assertEqual(second_response.status_code,202)
        self.assertTrue(response['content_type'], "application/json")
        result = json.loads(second_response.data.decode())
        self.assertEqual(
            result['message'],"User already exists.Please login"
        )
    
    def test_user_login(self):
        """Test registered user can login."""
        response = self.client.post('/api/v1/register', content_type='application/json',
         data=self.user_reg)
        self.assertEqual(response.status_code,201)
        login_response = self.client.post('/api/v1/login', data=self.user_data)
        result = json.loads(login_response.data.decode())
        self.assertEqual(result['message'], "You loggged in successfully")
        self.assertEqual(login_response.status_code,200)
        self.assertTrue(response['content_type'], "application/json")
        self.assertTrue(result['access_token'])

    def test_non_registered_user_login(self):
        """Test non registered users cannnot login."""
        not_a_user = {
            'email':'not_a_user@hmail.com',
            'password':'none'

        }
        response = self.client.post('/api/v1/login', content_type='application/json',
        data = not_a_user)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code,401)
        self.assertTrue(response['content_type'], "application/json")
        self.assertEqual(result['message'],"invalid email or password,please try again")

    def register_user(self,email='racheal@gmail.com',password='Racheal'):
        """This helps in registering a user"""
        user_data = {
            'email':email,
            'password':password
            }
        return self.client.post('/api/v1/login',data=user_data)

    def test_user_status(self):
        """Test for user status"""
        response = self.client.post('/api/v1/register', content_type='application/json',
        data=self.user_reg)
        login_response = self.client.get('/api/v1/status', headers = dict(Authorization=' Bearer'+
        json.loads(response.data.decode()) ['auth_token']))
        data = json.loads(login_response.data.decode())
        self.assertTrue(data['status'] == 'success')
        self.assertTrue(data['data'] is not None)
        self.assertTrue(data['data']['email'] == 'racheal@gmail.com')
        self.assertTrue(data['data']['admin'] is 'true' or 'false')
        self.assertEqual(response.status_code, 200)

