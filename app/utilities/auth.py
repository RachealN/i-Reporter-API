from flask import request,jsonify
from app.models.user_model import UserModel
import os 
import datetime
import jwt
from functools import wraps
import app


uzer = UserModel()
class AuthHelper:
    
    def __init__(self):
        self.secret_key = "thisismyireportersecretkey"

    def encode_auth_token(self, user_id):
        """Generates the access Token"""     

        payload = jwt.encode({
                
                'sub': user_id,
                'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)},
                    self.secret_key).decode('utf-8'),
                
        return payload

    
    def decode_token(self,payload):
        """Decodes the access token from the Authoriazation header"""
        Token = jwt.decode(payload, self.secret_key, algorithms=['HS256'])
        return Token
        

    
    def token_required(self,f):
        @wraps(f)
        def decorated(*args, **kwargs):
            payload = None
            
            
            if 'Authorization' in request.headers:
                payload = request.headers['Authorization'].split(" ")[1]
                
            if not payload:
                return jsonify({'message':'Token is missing'}), 401
                
                  
            # data = jwt.decode(payload,self.secret_key)
                

            try:
                
                data = jwt.decode(payload,self.secret_key)
                new_user = AuthHelper().encode_auth_token('user_id')
                isAdmin = AuthHelper().encode_auth_token('admin')
               
            except:
                return jsonify({'message':'Token is invalid'}),401
            return f(isAdmin,new_user,*args)
        return decorated



    def requires_auth(self,username,password):
        if username and password:
            return username == 'user' and password == 'user'
        # return username == 'admin' and password == 'admin'
    
    
    

    def user_auth_required(self,f):
        @wraps(f)
        def user_decorator(*args,**kwargs):
            auth = request.authorization
            user_auth = AuthHelper()
           
            if not auth: 
                return jsonify({'message':'Authenticate'})

            elif not user_auth.requires_auth(auth.username, auth.password):
                
                return jsonify({'message':'Authentication is required'}),401

            return f(*args, **kwargs)

        return user_decorator


    
