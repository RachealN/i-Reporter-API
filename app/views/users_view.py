from flask import Blueprint,request,json,jsonify
from app.controller.user_controller import UserController
from app.utilities.auth import AuthHelper


Auth_blueprint = Blueprint("Auth_blueprint", __name__)

user_controller = UserController()
required = AuthHelper()




@Auth_blueprint.route('/users', methods = ["GET"])
@required.token_required
def get_all_users(current_user):
    """Endpoint for getting all users"""

    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return jsonify({'user':user_controller.get_all_users()})    








@Auth_blueprint.route('/users/<int:user_id>', methods = ["GET"])
@required.token_required
def get_user(current_user,user_id):
    """Endpoint for getting a single user"""
    
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return jsonify({'user':user_controller.get_user_by_id(user_id)})
        



@Auth_blueprint.route('/users/<int:user_id>', methods = ["PUT"])
@required.token_required
def update_user(current_user,user_id):
    """Endpoints for updating  a user"""
    
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return jsonify({
        'user':user_controller.update_user(current_user) 
        })
    



@Auth_blueprint.route('/users/<int:user_id>', methods = ["DELETE"])
@required.token_required
def Delete_user(current_user,user_id):
    """Endpoints for Deleting  a user"""
    
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return jsonify({
            'user':user_controller.delete_user(user_id) 
            })
    




@Auth_blueprint.route('/register', methods = ["POST"])
def register_user():
    """Handle POST request for this Endpoint. Url ---> /api/v1/register"""
    
    request_data = request.get_json()
    return user_controller.register_user(request_data),201
    
    
    

@Auth_blueprint.route('/login', methods = ["POST"])
def login_user(): 
    """Handle POST request for this Endpoint. Url ---> /api/vi/login"""

    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            access_token = auth_header.split(" ")[1]

        except IndexError:
            return jsonify({
                'message':'Bearer token malformed.'
            })

    else:
        access_token = ''

    request_data = request.get_json()
    return user_controller.login(access_token, request_data),201
    
