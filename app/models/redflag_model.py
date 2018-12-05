from flask import abort
import datetime


class RedFlagBase:
    id = 0
    def __init__(self, createdBy,location,incidentType, status):
        self.createdBy = createdBy
        self.location = location
        self.incidentType = incidentType
        self.status = status
        RedFlagBase.id += 1
        self.createdOn = datetime.datetime.now()

class RedFlag:
    def __init__(self,base,image,video,comment):
        self.base =base
        self.image = image
        self.video = video
        self.comment = comment

    def redflag_json(self):
        return {
            "image": self.image,
            "video": self.video,
            "comment": self.comment,
            "createdBy":self.base.createdBy,
            "location": self.base.location,
            "incidentType":self.base.incidentType,
            "status":self.base.status

        }


class RedflagData:
    def __init__(self):
        self.redflags_list = []

    def create_redflag(self,redflag):
        for redflag in self.redflags_list:
            if redflag not in self.redflags_list:
                return redflag.append(redflag)
        # return self.redflags_list.append(redflag)

    def get_redflags(self):
        return self.redflags_list

    def get_single_redflag_by_id(self,id):
        for redflag in self.redflags_list:
            if redflag.id == id:
                return redflag
        return None

    def get_redflags_json(self):
        return [redflag.redflag_json for redflag in self.redflags_list]

    def patch_redflag_by_comment(self,id,comment):
         for redflag in self.redflags_list:
            if redflag.get("id") == id:
                redflag.update({"comment":comment})
                return redflag

    def patch_redflag_by_location(self,id,location):
        for redflag in self.redflags_list:
            if redflag.get("id") == id:
                redflag.update({"location":location})
                return redflag

    def delete_redflag(self,id):
         for redflag in self.redflags_list:
            if redflag.get ("id") == id:
                redflag.remove(redflag)
                return redflag










    