import os
from dotenv import load_dotenv
load_dotenv()
def getHeader():
    key,secret = [os.getenv("key"), os.getenv("secret")]
    headers = {
        'Content-Type': 'application/json',
        'X-Codeforces-API-KEY': key,
        'X-Codeforces-API-Secret': secret,
    }
    
    return headers
