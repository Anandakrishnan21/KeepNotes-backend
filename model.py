from pydantic import BaseModel
#pydantic auto create json schema for the model.

class test(BaseModel):
    title: str
    description: str
    email: str