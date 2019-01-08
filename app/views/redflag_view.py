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
@required.token_required
def create_redflag(new_user,isAdmin):
    if new_user is not isAdmin:
        return jsonify({
            'message':'You  cannot perform this function'
        }),200
    return jsonify({'Data':RedflagController.create_redflag(redflags)}),201

    

@redflag_blueprint.route('/red-flags', methods = ['GET'])
@required.token_required
def get_redflags(new_user):
    return redflags.get_redflags(),200
    
  
@redflag_blueprint.route('/red-flags/<int:id>',methods = ['GET'])
@required.token_required 
def get_single_redflag_by_id(new_user):
   return redflags.get_redflag_by_id(new_user),200
    

@redflag_blueprint.route('/red-flags/<int:id>/location',methods = ['PATCH'])
@required.token_required
def edit_redflag_location(new_user):
    return redflags.patch_redflag_by_location(new_user),200
    
    

@redflag_blueprint.route('/red-flags/<int:id>/comment',methods = ['PATCH'])
@required.token_required
def edit_redflag_comment(new_user):
    return redflags.patch_redflag_by_comment(new_user),200
    
    
@redflag_blueprint.route('/red-flags/<int:id>',methods = ['DELETE'])
@required.token_required
def delete_redflag(new_user):
    return redflags.delete_redflag(new_user),200
   























































































































































































































