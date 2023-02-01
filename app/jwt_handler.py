import jwt
import time
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Functions returns genrated tokens
def tokens(token:str):
    return {"access_token": token}


def signjwt(userID: str):
    payload = {
        "userID" : userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return tokens(token)



def decodejwt(token: str):
    try:
            
        deccode_jwt = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return deccode_jwt if deccode_jwt['expires'] >= time.time() else None
    except:
        return {}
    
