from pydantic import BaseModel
# defining structure of the datatype
#base model is the automatic class type 

class Message(BaseModel):
    name: str