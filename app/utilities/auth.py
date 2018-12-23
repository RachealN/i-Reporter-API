from flask import request,jsonify,make_response
import os 
import datetime
import jwt
import app


class AuthHelper():
    def __init__(self):
        self.secret_key = "thisismysecretkey"

    def encode_auth_token(self, user_id):
        
        auth = request.authorization
        if auth and auth.password == 'password':
            payload = jwt.encode({
                'user':auth.username,
                'sub': str(user_id), 
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, self.secret_key)
        
                
            return jsonify({'token':payload.decode('UTF-8')})
        return make_response('couldnot verify!',401,{'www-Authenticate':'Basic realm="login Required'})

    def decode_auth_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, self.secret_key)
            
            return payload['sub']
        
        except jwt.ExpiredSignatureError:
            return 'The token has expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'invalid token. Please login again'