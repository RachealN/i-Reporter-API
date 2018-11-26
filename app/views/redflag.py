from flask import Blueprint,request,jsonify
from app.models.redflag_model import RedFlag
from app.data.data import create_id,redflags
import datetime



redflag_blueprint = Blueprint("redflag_blueprint", __name__)
redflag = RedFlag()

@redflag_blueprint.route('/red-flags', methods = ["POST"])
def create_redflag():
    request_data = request.get_json()
    id = create_id(redflags)
    createdOn =datetime.datetime.now()
    createdBy = request_data.get("createdBy")
    location = request_data.get("location")
    status = request_data.get("status")
    incidentType = request_data.get("incidentType")
    comment = request_data.get("comment")
   

    redflag.create_redflag(id,createdOn,createdBy,location,status,incidentType,comment)
    request_data.update({"createdOn":createdOn})
    request_data.update({"id":id})

    data_list = []
    data_list.append(request_data)

    response = {
        "status":200,
        "data": data_list,
        "message":"Redflag created succesfully"

    }
    return jsonify(response)

@redflag_blueprint.route('/red-flags', methods = ['GET'])
def get_redflag():


    response = {
        "status":200,
        "data": redflag.get_redflags(),
        "message":" Get all Redflags succesful"

    }

    return jsonify(response)






























































































































































































































