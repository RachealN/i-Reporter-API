from flask import Blueprint,request,json,jsonify
from app.models.redflag_model import RedFlag
from app.models.redflag_model import RedFlag,RedFlagBase,RedflagData
# from app.data.data import create_id,redflags
from app.exception import InvalidUsage
import datetime
from app.controller.redflag_controller import RedflagController
import re

    

redflag_blueprint = Blueprint("redflag_blueprint", __name__)
redflags = RedflagController()
redflagslist = RedflagData()
redflag = redflagslist


@redflag_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"Welcome to I-Reporter"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags', methods = ["POST"])
def create_redflag():
    return jsonify({'status':201, 'Data':redflagslist.create_redflag(redflags),
        'message':'Redflag created successfully'})
   
    



@redflag_blueprint.route('/red-flags', methods = ['GET'])
def get_redflags():
    response = {
        "status":200,
        "data": redflags.get_redflags(),
        "message":" Get all Redflags succesful"

    }

    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>',methods = ['GET'])
def get_single_redflag_by_id(id):
   
    
    response = {
        "status":200,
        "data": redflags.get_redflag_by_id(id),
        "message":"Get a redflag by id succesful"

    }
    
    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>/location',methods = ['PATCH'])
def edit_redflag_location(id):
    response = {
        "status":200,
        "data": redflags.patch_redflag_by_location,
        "message":"Edit location succesfully"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>/comment',methods = ['PATCH'])
def edit_redflag_comment(id):
    response = {
        "status":200,
        "data": redflags.patch_redflag_by_comment,
        "message":"Edit comment succesful"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>',methods = ['DELETE'])
def delete_redflag(id):
    
    response = {
        "status":200,
        "data": redflags.delete_redflag(id),
        "message":"Redflag deleted succesfully"

    }
    return jsonify(response)
























































































































































































































