#main file
import uvicorn
from fastapi import FastAPI ,Depends
from app.schemas import CreatePost, UserSchema 
from app.jwt_handler import signjwt
from app.jwt_bearer import jwtBearer 

users = [{
    "id": 1,
    "user_name": "killingfreak",
    "password" : "Mahaveer"
}]

posts = [{
    "id":1,
    "title":"Jwt Tokens",
    "post":"Trying to use JwtTokens."
},
         {
    "id":2,
    "title":"Jwt Tokens uses",
    "post":"Authentication and data sharing."
},
         {
    "id":3,
    "title":"Jwt Tokens",
    "post":"jwt tokens are awsome and very easy to use."
}]




app = FastAPI()






@app.get("/show")
def ShowAll():
    return posts


@app.get("/get/{id}")
def Show(id:int):
    print(id , len(posts))
    for post in posts:
        if post['id'] == id:
            return post
        else:
            return{"oops": "not found !"}
        
@app.post('/create', dependencies =[Depends(jwtBearer())])
def Insert(request:CreatePost):
    post = {
        "id": len(posts) + 1,
        "title": request.title,
        "post": request.post
    }
    posts.append(post)
    return{"created" : "post"}

@app.delete("/destroy/{id}")
def destroy(id: int):
    for post in posts:
        if post["id"]==id:
            posts.remove(post)
            return{"deleted" : "object"}
        return{"oops": "not found"}



@app.post("/user/create_user", tags=["user"])
def create_user(request:UserSchema):
    user = {
        "id" : len(users) +1,
        "user_name" : request.user_name,
        "password" : request.password
    }
    users.append(user)
    return {"welcome" : request.user_name}


def check_user(request:UserSchema):
    for user in users:
        if user['user_name']==request.user_name and user['password'] == request.password:
            return True
        return False
    
@app.post('/user/login', tags=['user'])
def login(request:UserSchema):
    if check_user(request):
        return signjwt(request.user_name)
    return{"oops": "invalid credencials"}
