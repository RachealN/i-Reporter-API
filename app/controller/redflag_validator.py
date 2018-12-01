import re
from app.exception import InvalidUsage
from flask import request
from app.views.redflag_view import create_redflag


class RedFlagValidator:
    def __init__(self, id, createdBy,location,status,incidentType,comment,image,video):
        pass
        
       
    
    def validate_redflag_input_data(self):
        self.createdBy = request_data.get("createdBy")
        if not self.createdBy or self.createdBy.isspace():
            raise InvalidUsage('createdBy is required', status_code=400)
            
            charset = re.compile('[A-Za-z]')
            checkmatch = charset.match(self.createdBy)
        if not checkmatch:
            raise InvalidUsage('createdBy must be letters', status_code=400)
        
      






