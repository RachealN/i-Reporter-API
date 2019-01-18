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
        
        """function to create a redflag"""
    


        request_data = request.get_json()
        
        id = len(redflagslist.redflags_list) + 1
        location = request_data.get("location")
        incidentType = "redflag"
        image = request_data.get("image")
        video = request_data.get("video")
        status = "draft"
        comment = request_data.get("comment")

        if not validation_input.validate_integer_input(location):
            return ({
                "message": "location should be an integer or should not be empty"
                }),400
        if not validation_input.validate_string_input(comment):
            return ({
                "message": "comment should be a string or should not be empty"
                }),400

        if not validation_input.validate_string_input(image):
            return ({
                "message": "image should be a string or should not be empty"
                }),400

        if not validation_input.validate_string_input(video):
            return ({
                "message": "video should be a string or should not be empty"
                }),400

        
        my_redflag = RedFlag(RedFlagBase(video,incidentType,status),image,location,comment,id)
        redflagslist.create_redflag(my_redflag)


       
        return ({
            "status":201, 
            "request_data": my_redflag.redflag_json(),
            "message":"Created red-flag record"
        })

    
    
    def get_redflags(self):
        """function to get all redflags"""
        
        if len(redflagslist.redflags_list) < 1:
            return jsonify({
                "status":200,
                "message":"Redflag not found"
            })
        return jsonify ({
            "status": 200,
            "data": [redflag.redflag_json() for redflag in redflagslist.redflags_list]
            })
       
    
    def get_redflag_by_id(self, id):
        """function to get a single redflag"""
       
       
        redflug = redflagslist.get_single_redflag_by_id(id)
        if len(redflagslist.redflags_list) < 1 or redflug is None:
            return jsonify({
                "Message":"Redflag with that id is not found"
            })
        return jsonify({
            "status":200,
            "data": redflug.redflag_json()
        })

   
    def patch_redflag_by_comment(self,id):
        """function to edit comment
        :returns success message"""

        
        data = request.get_json()
        redflug = redflagslist.get_single_redflag_by_id(id)
        
        if redflug:
            comment = data["comment"]
            redflug.comment = comment
            return jsonify({
                "status" : 200,
                "message": "Updated red-flag record’s comment."
                })
        return jsonify({
                "status" : 200,
                "message": "red-flag comment with that id is not found."
                })

        
       
    def patch_redflag_by_location(self,id):

        """function to edit location"""
       

        data = request.get_json()
        redflug = redflagslist.get_single_redflag_by_id(id)
        if redflug:
            location = data["location"]
            redflug.location = location
            return jsonify({
                "status" : 200,
                "message":" Updated red-flag record’s location."
                })
        return jsonify({
            "status" : 200,
                "message":" red-flag location with that id not found."

        })
        
        
       
    def delete_redflag(self,user_id):
        """function to delete a redflag"""
        
        redflug = redflagslist.get_single_redflag_by_id(user_id)
        if redflug:
            redflagslist.redflags_list.remove(redflug)
            return jsonify({
                "messsage":"red-flag record has been deleted",
                "status":200
               })
        return jsonify({
            "Message":"Redflag with that id doesnot exist",
            "status":200
        })
               

        
        
        