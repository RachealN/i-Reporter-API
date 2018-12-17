from flask import request, jsonify,make_response
from app.models.user_model import UserModel
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

        
        

    def login(self, user_id, args):

        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('could not verify',401,{'www-Authenticate':'Basic realm="Login required!"'})

        new_user = self.auth_helper.encode_auth_token(user_id)
       
        
        
        if not new_user:
            return make_response('could not verify',401,{'www-Authenticate':'Basic realm="Login required"'})

        if check_password_hash(new_user.password, auth.password):
            return make_response('could not verify',401,{'www-Authenticate':'Basic realm="Login required"'})
        
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

    