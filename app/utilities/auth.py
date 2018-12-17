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
        
            
    # def decode_auth_token(self, authtoken):
    #     try:
    #         payload = jwt.decode(authtoken, self.secret_key)

    #         return payload['sub']
        
    #     except jwt.ExpiredSignatureError:
    #         return 'The token has expired. Please log in again'
    #     except jwt.InvalidTokenError:
    #         return 'invalid token. Please login again'
    
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
                # new_user = user_model.get_user_by_id(data('user_id')
                new_user = data.encode_auth_token('user_id')

            except:
                return jsonify({'message':'Token is Invalid'}),401

            return f(new_user,*args)

        return decorated

