import os
from dotenv import load_dotenv
load_dotenv()
def getAcessToken():
    accessToken = os.getenv("ACESS_TOKEN")
    return accessToken