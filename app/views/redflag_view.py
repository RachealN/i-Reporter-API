import datetime
from flask import Blueprint,request,json,jsonify,flash
from app.models.redflag_model import RedFlag
from app.models.redflag_model import RedFlag,RedFlagBase,RedflagData
from app.controller.redflag_controller import RedflagController
from app.utilities.auth import AuthHelper


    

redflag_blueprint = Blueprint("redflag_blueprint", __name__)
redflags = RedflagController()
required = AuthHelper()


"""Endpoint for the index page"""
@redflag_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"Welcome to I-Reporter"

    }
    return jsonify(response)


"""Endpoint for creating a redflag"""
@redflag_blueprint.route('/red-flags', methods = ["POST"])
@required.token_required
def create_redflag(current_user):
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return jsonify({'Data':RedflagController.create_redflag(redflags)}),201

    
"""Endpoint for getting all redflags"""
@redflag_blueprint.route('/red-flags', methods = ['GET'])
@required.token_required
def get_redflags(current_user):
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return redflags.get_redflags(),200
    

"""Endpoint for getting a single redflag""" 
@redflag_blueprint.route('/red-flags/<int:id>',methods = ['GET'])
@required.token_required 
def get_single_redflag_by_id(current_user,id):
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return redflags.get_redflag_by_id(id),200
    


"""Endpoint for editing  a location"""
@redflag_blueprint.route('/red-flags/<int:id>/location',methods = ['PATCH'])
@required.token_required
def edit_redflag_location(current_user,id):
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return redflags.patch_redflag_by_location(id),200
    
    
"""Endpoint for editing  a comment"""
@redflag_blueprint.route('/red-flags/<int:id>/comment',methods = ['PATCH'])
@required.token_required
def edit_redflag_comment(current_user,id):
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return redflags.patch_redflag_by_comment(id),200
    

"""Endpoint for  deleting a redflag"""    
@redflag_blueprint.route('/red-flags/<int:id>',methods = ['DELETE'])
@required.token_required
def delete_redflag(current_user,id):
    current_user=current_user.get('sub')
    if current_user.get('isAdmin') is False:
        return jsonify({
            'message':'You  cannot perform this function'
        }),401
    else:
        return redflags.delete_redflag(id),200
   























































































































































































































