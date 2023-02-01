from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decodejwt


class jwtBearer(HTTPBearer):
    def __init__(self, auto_error : bool =True):
        super(jwtBearer, self).__init__(auto_error=auto_error)
        
    async def __call__(self, request:Request):
        credentials : HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
               raise HTTPException(status_code=403, detail="invalid or Expired token")
            return credentials.credentials
        else:
            raise HTTPException(status_code= 403 , details = "Invalid or expired")
        
    def verify(self, jwttoken: str):
        isTokenValid : bool = False   #False Flage
        payload = decodejwt(jwttoken)
        if payload:
            isTokenValid = True

