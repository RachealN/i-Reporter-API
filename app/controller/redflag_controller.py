from flask import request,jsonify
from app.models.redflag_model import RedFlagBase,RedFlag,RedflagData


redflagslist = RedflagData()


class RedflagController:
    def __init__(self):
        pass

    def create_redflag(self):
        request_data = request.get_json()
        createdBy = request_data.get("createdBy")
        location = request_data.get("location")
        incidentType = request_data.get("incidentType")
        image = request_data.get("image")
        video = request_data.get("video")
        status = request_data.get("status")
        comment = request_data.get("comment")
#validation
        my_redflag = RedFlag(RedFlagBase(createdBy,location,incidentType,status),image,video,comment)
        redflagslist.create_redflag(my_redflag)
        return jsonify({
            "message":"Redflag created successfully", 
            "request_data": my_redflag.redflag_json(),
            "status":201
        })


    def get_redflags(self):
        return redflagslist.get_redflags()
    
    def get_redflag_by_id(self,id):
        for redflag in redflagslist.get_redflags():
            if redflag['id']==id:
                return redflagslist.get_single_redflag_by_id(id)
            return None
   
    def patch_redflag_by_comment(self,id,comment):
         request_data = request.get_json()
         self.comment = request_data.get("comment")

         redflagslist.patch_redflag_by_comment(id,comment)
         redflags_list = []
         redflags_list.append(redflagslist.patch_redflag_by_comment)
         return redflagslist.patch_redflag_by_comment(id,comment)
       

    def patch_redflag_by_location(self,id,location):
        request_data = request.get_json()
        self.location = request_data.get("location")

        redflagslist.patch_redflag_by_location(id,location)
        redflags_list = []
        redflags_list.append(redflagslist.patch_redflag_by_location)
        return redflagslist.patch_redflag_by_location(id,location)

    def delete_redflag(self, redflag):
        redflags_list = []
        redflags_list.append(redflag.delete_redflag(id))