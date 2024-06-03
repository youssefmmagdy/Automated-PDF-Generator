from decouple import config

CLIENT_ID = config("CLIENT_ID", default=False)
CLIENT_SECRET = config("CLIENT_SECRET", default=False)
BASE_API_URL = config("BASE_API_URL", default=False)