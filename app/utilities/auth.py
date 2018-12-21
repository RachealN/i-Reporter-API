from flask import request,jsonify,make_response
import os 
import datetime
import jwt
from functools import wraps
import app



class AuthHelper:
    
    def __init__(self):
        self.secret_key = "thisismyireportersecretkey"

    def encode_auth_token(self, user_id):
        """Generates the access Token"""     

        payload = jwt.encode({
                
                'sub': user_id,
                'iat':datetime.datetime.now(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
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
            
            
            if 'access_token' in request.headers:
                payload = request.headers['access_token']
            
            if not payload:
                return jsonify({'message':'Token is missing'}), 401

            try:
                data = jwt.decode(payload,self.secret_key)
                new_user = data.encode_auth_token('user_id')

            except:
                return jsonify({'message':'Token is Invalid'}),401

            return f(new_user,*args)

        return decorated

