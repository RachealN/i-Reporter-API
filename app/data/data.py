redflags = []

def create_id(redflags):
    id = 1
    for redflag in redflags:
        if redflag.get("id") == id:
            id=id+1

    return id




