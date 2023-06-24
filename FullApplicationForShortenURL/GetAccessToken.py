import os
from dotenv import load_dotenv
load_dotenv()
def getAccess():
    return os.getenv("accessToken")
