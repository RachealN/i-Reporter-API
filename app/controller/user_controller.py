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

        


    # def login(self):
    #     data = request.get_json()
    #     for user in myuser_list:
    #         if data['username'] == user["username"]:
    #             return "HELLO"
    #         else:
    #             return "This didn't workout my brother"

        # user_model = UserModel()
        
        # # auth_header = request.headers.get('Authorization')
        # # access_token = auth_header.split(" ")[1]

        # request_data=request.get_json()
        # try:
        #     user = user_model.get_user_by_id(user_id)
        #     if user and user.user_id(request_data['user_id']):
                
        #         access_token = user.encode_auth_token(user_id)
        #         if access_token:
        #              response = {
        #                 'message': 'You logged in successfully.',
        #                 'access_token': access_token.decode()
        #             }
        #         return make_response(jsonify(response)), 200

        #     else:
        #         response = {
        #             'message': 'Invalid email or password, Please try again'
        #         }
        #         return make_response(jsonify(response)), 401

    
        # except Exception as Error:
        #     response = {
        #         'message': str(Error)
        #     }
        #     return make_response(jsonify(response)), 500



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

    