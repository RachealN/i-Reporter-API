from flask import request,jsonify,make_response
import os 
import datetime
import jwt
from functools import wraps
import app



class AuthHelper:
    def __init__(self):
        self.secret_key = "thisismysecretkey"

    def encode_auth_token(self, user_id):
        
       
        try:
            payload = jwt.encode ({
                'user':auth.username,
                'sub': str(user_id), 
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
                },self.secret_key)
            return jsonify({'Token':payload.decode('UTF-8')})
        
        except Exception as identifier:
            return identifier
        
        
    
    def token_required(self,f):
        @wraps(f)
        def decorated(*args):
            payload = None
            
            if 'x-access-token' in request.headers:
                payload = request.headers['x-access-token']
            
            if not payload:
                return jsonify({'message':'Token is missing'}), 401

            try:
                data = jwt.decode(payload,self.secret_key)
                new_user = data.encode_auth_token('user_id')

            except:
                return jsonify({'message':'Token is Invalid'}),401

            return f(new_user,*args)

        return decorated

