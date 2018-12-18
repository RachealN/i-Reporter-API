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
        """Generates the access Token"""
        try:
            payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id  
            }
            token = jwt.encode(
                payload,
                self.secret_key,
                algorithm='HS256'
            )
            return token
        
        except Exception as Error:
            return str(Error)

    
    def decode_token(self,token):
        """Decodes the access token from the Authoriazation header"""
        
        try:
            payload = jwt.decode(token,self.secret_key)
            return payload['sub']
        
        except jwt.ExpiredSignatureError:
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"


    
        
        
    
    # def token_required(self,f):
    #     @wraps(f)
    #     def decorated(*args):
    #         payload = None
            
    #         if 'x-access-token' in request.headers:
    #             payload = request.headers['x-access-token']
            
    #         if not payload:
    #             return jsonify({'message':'Token is missing'}), 401

    #         try:
    #             data = jwt.decode(payload,self.secret_key)
    #             new_user = data.encode_auth_token('user_id')

    #         except:
    #             return jsonify({'message':'Token is Invalid'}),401

    #         return f(new_user,*args)

    #     return decorated

