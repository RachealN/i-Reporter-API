from flask import request, jsonify,make_response, json
from app.models.user_model import UserModel,users
from app.utilities.auth import AuthHelper
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import jwt
import re

class UserController:
    user_list = UserModel()
    auth_helper = AuthHelper()
    


    def __init__(self):
        self.users = []
        
    
    def register_user(self,args):
        
        
        user = self.user_list.add_user(args)
        

        user_id = user['user_id']
        auth_token = self.auth_helper.encode_auth_token(user_id) 
        if not user or user is None:
            return jsonify({
                'message':'user was not created',
                "status": 400
            })


        return jsonify({
            "status": 201,
            'message': 'user has been succesfully created' ,
            'users': user
    
        })

       
        


    def login(self,access_token,args):
        request_data = request.get_json()
        
        for  user in users:
            if request_data['email'] == user['email'] and request_data['password'] == user['password'] :
                return  jsonify({
                        'Token': self.auth_helper.encode_auth_token(user)
                    })

            return jsonify({
                'message':'Invalid email or password, Please try again',
                
                
                })
        return jsonify({'message':'Not registered,please register first before logging in'})
        
    
            
        

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
    def delete_user(self,user_id):
        user_model = UserModel()
        user = user_model.get_user_by_id(user_id)
        if user:
            user_model.users.remove(user)
            return ({
                "messsage":"user has been deleted succesfully",
                "status":200
               })
        return ({
            "Error":"user with that user_id doesnot exist",
            "status":200
        })

    def update_user(self,user_id):
        user_model =UserModel()
        user = user_model.get_user_by_id(user_id)
        try:
            user = user_model.get_user_by_id(user_id)
            if user:
                user = user_model.users.update(user)
                return ({
                    "messsage":"user has been updated succesfully",
                    "status":200
                })

            return ({
                "Error":"user with that user_id doesnot exist",
                "status":200
            })

        except:
            return ({
                'error': 'user has not been updated',
                'status':401
            })
            


                

    


    