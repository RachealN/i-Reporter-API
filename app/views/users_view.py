from flask import Blueprint,request,json,jsonify
from app.controller.user_controller import UserController



Auth_blueprint = Blueprint("Auth_blueprint", __name__)

user_controller = UserController()

@Auth_blueprint.route('/users', methods = ["GET"])
def get_all_users():
    return jsonify({
        'user': user_controller.get_all_users()
    }),200
    

@Auth_blueprint.route('/users/<int:user_id>', methods = ["GET"])
def get_user(user_id):
    return jsonify({
        'user': user_controller.get_user_by_id(user_id)
    })
    

    

@Auth_blueprint.route('/register', methods = ["POST"])
def register_user():
    request_data = request.get_json()
    return user_controller.register_user(request_data),201
    
    

@Auth_blueprint.route('/login', methods = ["POST"])
def login_user(user_id):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]

        except IndexError:
            return jsonify({
                'message':'Bearer token malformed.'
            })

    else:
        auth_token = ''

    data = request.get_json()
    return user_controller.login(auth_token, data)






