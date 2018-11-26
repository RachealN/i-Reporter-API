from flask import abort
from app.data.data import redflags

class RedFlag:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.createdOn = kwargs.get("createdON")
        self.createdBy = kwargs.get("createdBy")
        self.location = kwargs.get("location")
        self.incidentType = kwargs.get("incidentType")
        self.status = kwargs.get("status")
        self.comment = kwargs.get("comment")

    def create_redflag(self,id,createdOn,createdBy,location,incidentType,status,comment):
        redflag = {
            "id":id,
            "createdOn":createdOn,
            "createdBy":createdBy,
            "location":location,
            "incidentType":incidentType,
            "status":status,
            "comment":comment
            }
        
        redflags.append(redflag)

    def get_single_redflag_by_id(self,id):
        for redflag in redflags:
            if redflag.get ("id") == id:
                return redflag


    def patch_redflag_location(self,id,location):
        for redflag in redflags:
            if redflag.get("id") == id:
                redflag.update({"location":location})
                return redflag

    def patch_redflag_comment(self,id,comment):
        for redflag in redflags:
            if redflag.get("id") == id:
                redflag.update({"comment":comment})
                return redflag

    