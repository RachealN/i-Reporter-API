from flask import request,jsonify
from app.models.redflag_model import RedFlagBase,RedFlag,RedflagData
from app.validations import Validator
import re



redflagslist = RedflagData()
validation_input = Validator()

class RedflagController:
    def __init__(self):
        pass

 
    def create_redflag(self):
        request_data = request.get_json()
        
        user_id = len(redflagslist.redflags_list) + 1
        location = request_data.get("location")
        incidentType = "redflag"
        image = request_data.get("image")
        video = request_data.get("video")
        status = "draft"
        comment = request_data.get("comment")

#validation
        if not validation_input.validate_string_input(location):
            return ({
                "message": "location should be a string"
                }),400
        if not validation_input.validate_string_input(comment):
            return ({
                "message": "comment should be a string"
                }),400

        if not validation_input.validate_string_input(incidentType):
            return ({
                "message": "incidentType should be a string"
                }),400

        
        my_redflag = RedFlag(RedFlagBase(location,incidentType,status),image,video,comment,user_id)
        redflagslist.create_redflag(my_redflag)

       
        return ({
            "status":201, 
            "request_data": my_redflag.redflag_json(),
            "message":"Redflag created successfully"
        })

    
    def get_redflags(self):
        if len(redflagslist.redflags_list) < 1:
            return jsonify({
                "status":200,
                "message":"Redflag not found"
            })
        return jsonify ({
            "status": 200,
            "data": [redflag.redflag_json() for redflag in redflagslist.redflags_list]
            })
       
    
    def get_redflag_by_id(self, user_id):
       
        red = redflagslist.get_single_redflag_by_id(user_id)
        if len(redflagslist.redflags_list) < 1 or red is None:
            return jsonify({
                "Error":"Redflag with id is not found"
            })
        return jsonify({
            "data": red.redflag_json()
        })

   
    def patch_redflag_by_comment(self,user_id):
        data = request.get_json()
<<<<<<< HEAD
        red = redflagslist.get_single_redflag_by_id(user_id)
        if red:
            comment = data["comment"]
            red.comment = comment
            return jsonify({
                "status" : 200,
                "message": "red-flag comment has been updated successfully."
                })
        return jsonify({
                "status" : 200,
                "message": "red-flag comment with that user_id is not found."
                })
       
    def patch_redflag_by_location(self,user_id):
        data = request.get_json()
        red = redflagslist.get_single_redflag_by_id(user_id)
        if red:
            location = data["location"]
            red.location = location
            return jsonify({
                "status" : 200,
                "message":" red-flag location location has been updated successfully."
                })
        return jsonify({
            "status" : 200,
                "message":" red-flag location with that id not found."

        })
        
        
       
=======
        red = redflagslist.get_single_redflag_by_id(user_id)
        comment = data["comment"]
        red.comment = comment
        return jsonify({
            "status" : 200,
            "message":"Updated red-flag record's comment."
            })
        
       
    def patch_redflag_by_location(self,user_id):
        data = request.get_json()
        red = redflagslist.get_single_redflag_by_id(user_id)
        location = data["location"]
        red.location = location
        return jsonify({
            "status" : 200,
            "message":"Updated red-flag record's location."
            })
        
       
>>>>>>> 5e041fd78a4e53ed338e324284fa5379ac1c0681
    def delete_redflag(self,user_id):
        red = redflagslist.get_single_redflag_by_id(user_id)
        if red:
            redflagslist.redflags_list.remove(red)
            return jsonify({
                "messsage":"Redflag has been deleted succesfully",
                "status":200
               })
        return jsonify({
            "Error":"Redflag with that user_id doesnot exist",
            "status":200
        })
               

        
        
        