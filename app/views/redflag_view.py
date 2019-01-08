from flask import Blueprint,request,json,jsonify,flash
from app.models.redflag_model import RedFlag
from app.models.redflag_model import RedFlag,RedFlagBase,RedflagData
import datetime
from app.controller.redflag_controller import RedflagController
import re
from app.utilities.auth import AuthHelper


    

redflag_blueprint = Blueprint("redflag_blueprint", __name__)
redflags = RedflagController()
required = AuthHelper()


@redflag_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"Welcome to I-Reporter"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags', methods = ["POST"])
@required.user_auth_required
def create_redflag():
    return jsonify({'Data':RedflagController.create_redflag(redflags)}),201

    

@redflag_blueprint.route('/red-flags', methods = ['GET'])
@required.user_auth_required
def get_redflags():
    return redflags.get_redflags(),200
    
   
@redflag_blueprint.route('/red-flags/<int:user_id>',methods = ['GET'])
@required.user_auth_required
def get_single_redflag_by_id(user_id):
   return redflags.get_redflag_by_id(user_id),200
    

@redflag_blueprint.route('/red-flags/<int:user_id>/location',methods = ['PATCH'])
@required.user_auth_required
def edit_redflag_location(user_id):
    return redflags.patch_redflag_by_location(user_id),200
    
    

@redflag_blueprint.route('/red-flags/<int:user_id>/comment',methods = ['PATCH'])
@required.user_auth_required
def edit_redflag_comment(user_id):
    return redflags.patch_redflag_by_comment(user_id),200
    
    
@redflag_blueprint.route('/red-flags/<int:user_id>',methods = ['DELETE'])
@required.user_auth_required
def delete_redflag(user_id):
    return redflags.delete_redflag(user_id),200
   























































































































































































































