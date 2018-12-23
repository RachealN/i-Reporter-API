from flask import request, jsonify
from app.models.user_model import UserModel
from app.utilities.auth import AuthHelper
import datetime

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

        user_id = user['user_id']
        auth_token = self.auth_helper.encode_auth_token(user_id)  

        if not auth_token or auth_token is None:
            return jsonify({
                'message':'user was not created',
                "status": 400
            })


        return jsonify({
            "status": 201,
            'message': 'user created but not authenticated, please login first' ,
            'users': user
    
        })

        
        

    def login(self, auth_token, args):
        user_model = UserModel()

        if auth_token:
            user_id = auth_helper.decode_auth_token(auth_token)
            
            
            if not isinstance(user_id, str):
                return  jsonify({
                    'message':'wrong token'
                })

            user = user_model.get_user_by_id(int(user_id))
            if not user or user is None:
                return jsonify({
                    'message':'user not found'
                })
            return jsonify({
                'status':'logged in',
                'user':user
            })

        else:
            return jsonify({
                'message':'provide valid token'
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

    