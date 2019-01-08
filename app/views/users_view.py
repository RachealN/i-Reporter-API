from flask import Blueprint,request,json,jsonify,make_response
from app.controller.user_controller import UserController
from app.utilities.auth import AuthHelper


Auth_blueprint = Blueprint("Auth_blueprint", __name__)
user_controller = UserController()
required = AuthHelper()

@Auth_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"You are logged in"

    }
    return jsonify(response)

@Auth_blueprint.route('/users', methods = ["GET"])
@required.token_required
def get_all_users(new_user,isAdmin):
    if new_user is  isAdmin:
        return jsonify({
            'message':'You  cannot perform this function'
        }),200
    else:
        return jsonify({'user':user_controller.get_all_users()})    

@Auth_blueprint.route('/users/<int:user_id>', methods = ["GET"])
@required.token_required
def get_user(new_user,isAdmin):
    if new_user is isAdmin:
            return jsonify({
            'user': 'hello'
        })
    return jsonify({'user':user_controller.get_user_by_id(new_user)})
        
@Auth_blueprint.route('/users/<int:user_id>', methods = ["PUT"])
@required.token_required
def update_user(new_user):
    return jsonify({
       'user':user_controller.update_user(new_user) 
    })
    
@Auth_blueprint.route('/users/<int:user_id>', methods = ["DELETE"])
@required.token_required
def Delete_user(new_user):
    return jsonify({
       'user':user_controller.delete_user(new_user) 
    })
    

@Auth_blueprint.route('/register', methods = ["POST"])
def register_user():
    request_data = request.get_json()
    return user_controller.register_user(request_data),201
    
    
    

@Auth_blueprint.route('/login', methods = ["POST"])
def login_user(): 
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            access_token = auth_header.split(" ")[1]

        except IndexError:
            return make_response(jsonify({
                'message':'Bearer token malformed.'
            }))

    else:
        access_token = ''

    request_data = request.get_json()
    return user_controller.login(access_token, request_data),201
    
