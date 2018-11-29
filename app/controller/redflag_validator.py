

class RedFlagValidator:
    def __init__(self, id, createdBy,location,status,incidentType,comment):
        self.id = id
        self.createdBy = createdBy
        self.location = location
        self.status = status
        self.incidentType = incidentType
        self.comment = comment

    def validate_redflag_input_data(self):
        if not self.id or self.id.isspace() or self.id.isinstance('id',int):
            return 'id field can not be left empty or cannot be a string.'
        
        if not self.createdBy or self.createdBy.isspace():
            return 'createdBy field can not be left empty or cannot be an interger.'

        if not self.location or self.location.isspace() or self.location.isinstance('location',str):
            return 'location field can not be left empty or cannot be an interger.'

        if not self.status or self.status.isspace() or self.status.isinstance('status',str):
            return 'status field can not be left empty or cannot be an interger.'

        if not self.incidentType or self.incidentType.isspace() or self.incidentType.isinstance('incident',str):
            return 'incidentType field can not be left empty or cannot be an interger.'
           
        if not self.comment or self.comment.isspace() or self.comment.isinstance('comment',str):
            return 'comment field can not be left empty or cannot be an interger.'
           
           
           
           
        
        

    
    








