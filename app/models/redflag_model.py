from flask import abort,jsonify
import datetime


class RedFlagBase:
    def __init__(self,location,incidentType, status):
        self.location = location
        self.incidentType = incidentType
        self.status = status
        self.createdOn = datetime.datetime.now()
       

class RedFlag:
    def __init__(self,base,image,video,comment,user_id):
        self.base = base
        self.image = image
        self.video = video
        self.comment = comment
        self.user_id = user_id
    
    def redflag_json(self):
        return {
            "image": self.image,
            "video": self.video,
            "comment": self.comment,
            "user_id": self.user_id,
            "location": self.base.location,
            "incidentType": self.base.incidentType,
            "status": self.base.status,
            "createdon": datetime.datetime.now()
        }


class RedflagData:
    def __init__(self):
        self.redflags_list = []

    def create_redflag(self,redflag):
        return self.redflags_list.append(redflag)
    

    def get_redflags(self):
        return self.redflags_list

    def get_single_redflag_by_id(self, user_id):
        for redflag in self.redflags_list:
            if redflag.user_id == user_id:
                return redflag
        return None

    def get_redflag_json(self):
        return [redflag.redflag_json for redflag in self.redflags_list]

    
    









    