from flask import request,jsonify
from app.models.redflag_model import RedFlagBase,RedFlag,RedflagData
from app.exception import Valid
import re



redflagslist = RedflagData()


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
        
        request_data = request.get_json()

        red = redflagslist.get_single_redflag_by_id(user_id)

        red.red = request_data.get('comment')
        return jsonify({
                "data":[{"Success": "Updated red-flag record's comment."}],
                'status': 200
                }), 200
        
       
    def patch_redflag_by_location(self,id,location):
        pass
    

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
            "status":400
        })
               

        
        
        