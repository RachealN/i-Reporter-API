from flask import abort,jsonify
import datetime


class RedFlagBase:
    def __init__(self,video,incidentType, status):
        self.video = video
        self.incidentType = incidentType
        self.status = status
        self.createdOn = datetime.datetime.now()
       

class RedFlag:
    def __init__(self,base,image,location,comment,user_id):
        self.base = base
        self.image = image
        self.location = location        
        self.comment = comment
        self.user_id = user_id
    
    def redflag_json(self):
        return {
            "image": self.image,
            "location": self.location,
            "comment": self.comment,
            "user_id": self.user_id,
            "video": self.base.video,
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

    
    









    