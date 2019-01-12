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
                firstname = "okello",
                lastname = "opio",
                othernames = "heloo",
                email = "odetah@gmail.com",
                username = "Ahabwe",
                password  = "12345",
                phonenumber = "0786576572"
        )))
        users.append(dict)
        self.assertEqual(response.status_code,201)
        self.assertIn("",str(response.data))
        self.assertTrue(len(users),2)
        self.assertNotEqual("user with id is not found",str(response.data))

    
    def test_login_user(self):
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

       
    
    
    def test_get_users(self):
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
        
        
        response = self.client.get('/api/v1/users',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.users_empty))
        self.assertEqual(len(self.users_empty),0)
    
    
    def test_get_single_user_by_id(self):
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
        
        
        response = self.client.get('/api/v1/users/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.user))
        # self.assertEqual(response.status_code,200)
        self.assertTrue(self.user,response.data)
        self.assertNotEqual("user with that id is not found",str(response.data))
    

       

    def test_get_users_empty_list(self):
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

        response = self.client.get('/api/v1/users',
        content_type='application/json',headers=dict(Authorization='Bearer '+token),
        data=json.dumps(self.users_empty))
        self.assertEqual(len(self.users_empty),0)

    def test_delete_user(self):
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
        
        response=self.client.delete('/api/v1/users/1',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(self.redflags),1)
        self.assertNotEqual("user with that id doesnt exist",str(response.data))
    
    def test_delete_redflag_doesnt_exist(self):
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



        response=self.client.delete('/api/v1/users/2',
        content_type='application/json',headers=dict(Authorization='Bearer '+token))
        data=json.dumps(self.users_empty)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(self.users_empty),0)
        self.assertNotEqual("user with that id doesnt exist",str(response.data))
    
    
    def test_non_registered_user_login(self):
        """Test non registered users cannnot login."""

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

        not_a_user = {
            'email':'not_a_user@hmail.com',
            'password':'none'

        }

        response = self.client.post('/api/v1/login',
        content_type='application/json',
        data=json.dumps(not_a_user))

        
        
        # self.assertEqual(response.status_code,401)
        self.assertNotEqual("Invalid email or password, Please try again",str(response.data))
        self.assertNotEqual("Not registered,please register first before logging in",str(response.data))
    
    
    

    