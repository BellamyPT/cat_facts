import requests
from time import sleep

class Connector():
    def __init__(self) -> None:
        self.api_url = "https://catfact.ninja/fact"

    def extract_info(self) -> dict:
        sleep(1)
        response = requests.get(self.api_url)
        return response.json()

  