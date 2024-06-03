import os
import requests

from PDF4RoomKey.settings import CLIENT_ID, CLIENT_SECRET

class Authenticator:
    """
    Authenticator class for PDF4RoomKey
    It takes an url, client_id and client_secret as input and generates a bearer token.
    """

    DEFAULT_URL = "https://identity.apaleo.com/connect/token"

    @staticmethod
    def generate_bearer_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, url=DEFAULT_URL):
        """
        Generate a bearer token
        """

        response = requests.post(url, data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        })

        if response.status_code == 200:
            token = response.json()["access_token"]
            return token
        else:
            print("Error:", response.status_code)
            return None
