from flask import Blueprint,request,jsonify
from app.models.redflag_model import RedFlag
from app.data.data import create_id,redflags
from app.exception import InvalidUsage
# from app.controller.redflag_validator import RedFlagValidator
import datetime
import re



redflag_blueprint = Blueprint("redflag_blueprint", __name__)
redflag = RedFlag()

@redflag_blueprint.route('/')
def index():
    response = {
        "status":200,
        "message":"Welcome to I-Reporter"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags', methods = ["POST"])
def create_redflag(): 
    request_data = request.get_json()
    
    id = create_id(redflags)
    createdOn = datetime.datetime.now()
    createdBy = request_data.get("createdBy")
    location = request_data.get("location")
    status = request_data.get("status")
    incidentType = request_data.get("incidentType")
    image = request_data.get("image")
    video = request_data.get("video")
    comment = request_data.get("comment")
    
    createdBy = request_data.get("createdBy")
    
    if not createdBy or createdBy.isspace():
        return jsonify({"message":"This field is required"}),400
    charset = re.compile('[A-Za-z]')
    checkmatch = charset.match(createdBy)
    if not checkmatch:
        return jsonify({"message":"createdBy must be letters"}),400
           
    redflag.create_redflag(id,createdOn,createdBy,location,status,incidentType,comment,image,video)
    request_data.update({"createdOn":createdOn})
    request_data.update({"id":id})

    data_list = []
    data_list.append(request_data)

    response = {
            "status":201,
            "data": data_list,
            "message":"Redflag created succesfully"

        }
    return jsonify(response)
    



@redflag_blueprint.route('/red-flags', methods = ['GET'])
def get_redflag():

    response = {
        "status":200,
        "data": RedFlag.get_redflags(redflag.get_redflags),

        "message":" Get all Redflags succesful"

    }

    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>',methods = ['GET'])
def get_single_redflag_by_id(id):
    data_list = []
    data_list.append(redflag.get_single_redflag_by_id(id))
    
    response = {
        "status":200,
        "data": data_list,
        "message":"Get a redflag by id succesful"

    }
    
    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>/location',methods = ['PATCH'])
def edit_redflag_location(id):
    request_data = request.get_json()
    location = request_data.get("location")

    redflag.patch_redflag_location(id,location)

    data_list = []
    data_list.append(redflag.get_single_redflag_by_id(id))
    
    response = {
        "status":200,
        "data": data_list,
        "message":"Edit location succesfully"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>/comment',methods = ['PATCH'])
def edit_redflag_comment(id):
    request_data = request.get_json()
    comment = request_data.get("comment")

    redflag.patch_redflag_comment(id,comment)

    data_list = []
    data_list.append(redflag.get_single_redflag_by_id(id))
    
    response = {
        "status":200,
        "data": data_list,
        "message":"Edit comment succesful"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags/<int:id>',methods = ['DELETE'])
def delete_redflag(id):

    data_list = []
    data_list.append(redflag.delete_redflag(id))
    
    response = {
        "status":200,
        "data": data_list,
        "message":"Redflag deleted succesfully"

    }
    return jsonify(response)
























































































































































































































