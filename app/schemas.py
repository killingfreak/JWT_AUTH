from pydantic import BaseModel


class CreatePost(BaseModel):
    title : str
    post : str 
    

class UserSchema(BaseModel):
    user_name : str
    password : str