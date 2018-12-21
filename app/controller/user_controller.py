from flask import request, jsonify,make_response, json
from app.models.user_model import UserModel,myuser_list
from app.utilities.auth import AuthHelper
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import jwt

class UserController:
    user_list = UserModel()
    auth_helper = AuthHelper()


    def __init__(self):
        self.users = []
        
    
    def register_user(self,args):
    
 
        # user = self.user_list.add_user(args)
        # if not user:
        #     return jsonify({
        #         'message':'user was not created',
        #         "status": 400
        #     })
           

        # return jsonify({
        #     "status": 201,
        #     'message': 'user created successfully' ,
        #     'users': user
    
        # })
        
        
        user = self.user_list.add_user(args)

        # user_id = user['user_id']
        # auth_token = self.auth_helper.encode_auth_token(user_id)  

        if not user or user is None:
            return jsonify({
                'message':'user was not created',
                "status": 400
            })


        return jsonify({
            "status": 201,
            'message': 'user created but not authenticated, please login first' ,
            'users': user
    
        })


    def login(self,access_token,args):
        request_data = request.get_json()
 
        for  user in myuser_list:
            if request_data['email'] == user['email'] and request_data['password'] == user['password'] :
                return  jsonify({
                        'Token': self.auth_helper.encode_auth_token(user)
                    })

            return jsonify({
                'message':'Invalid username or password, Please try again'
                
                })
            
        

    def get_all_users(self):
        user_model = UserModel()

        users = user_model.get_all_users()
        if not users:
            return ({
                'message':'No users were found',
                'status':400
            })
        
        return ({
            'user': user_model.users,
            'status':200,
            'message':'success'
                })
        
    def get_user_by_id(self,userId):
        user_model = UserModel()

        user = user_model.get_user_by_id(userId)
        if not user:
            return({
               'status':200,
               'message':'user with that id not found'
           })
        return ({
            'status': 200,
            'message': 'success',
            'user': user
            })

    


    