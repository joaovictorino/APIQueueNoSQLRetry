import requests
import json
from requests.exceptions import HTTPError
from retry import retry

class StockService:

    def __init__(self, address):
        self.address = address

    @retry(HTTPError, tries=10)
    def call(self, body):
        response = requests.post(self.address, json=json.dumps(body))
        response.raise_for_status()
        return response.text.strip()