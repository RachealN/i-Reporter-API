from flask import Blueprint,request,json,jsonify



Auth_blueprint = Blueprint("Auth_blueprint", __name__)

@Auth_blueprint.route('/users', methods = ["POST"])
def user_signup(self):
    pass


@Auth_blueprint.route('/admin', methods = ["POST"])
def admin_signup(self):
    pass


@Auth_blueprint.route('/login', methods = ["post"])
def user_login(self):
    pass



