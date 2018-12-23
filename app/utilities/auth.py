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
            
            
            if 'access_token' in request.headers:
                payload = request.headers['access_token']
            
            if not payload:
                return jsonify({'message':'Token is missing'}), 401
                
            data = jwt.decode(payload,self.secret_key)
            print("$$$$$$$$$",data)

            if data:
                new_user = data.encode_auth_token('user_id')
                print("%%%%%%%%%",new_user)
            else:
                return jsonify({'message':'Token is invalid'}),401
            return f(new_user=1,*args)
        return decorated


        #     try:
        #         data = jwt.decode(payload,self.secret_key)
        #         new_user = data['user_id']
        #         print(new_user)
        #         # new_user = data.encode_auth_token('user_id')

        #     except:
        #         return jsonify({'message':'Token is Invalid'}),401

        #     return f(new_user,*args)

        # return decorated

    def requires_auth(self,username,password):
        return username == 'user' and password == 'secret'
    
    def admin_auth(self,username,password):
        return username == 'Admin' and password == 'secret'
    
    

    def user_auth_required(self,f):
        @wraps(f)
        def user_decorator(*args,**kwargs):
            auth = request.authorization
            user_auth = AuthHelper()
        
            
            if not auth: 
                return jsonify({'message':'Authentication is required'})

            elif not user_auth.requires_auth(auth.username, auth.password):
                
                return jsonify({'message':'Authentication is required'}),401
            
            return f(*args, **kwargs)

        return user_decorator


    def admin_auth_required(self,f):
        @wraps(f)
        def admin_decorator(*args,**kwargs):
            auth = request.authorization
            user_auth = AuthHelper()
        
            
            if not auth: 
                return jsonify({'message':'Authentication is required'})

            elif not user_auth.admin_auth(auth.username, auth.password):
                
                return jsonify({'message':'Authentication is required'}),401
            
            return f(*args, **kwargs)

        return admin_decorator

        

