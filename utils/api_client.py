import requests
from config.config import BASE_URL, HEADERS

class APIClient:

    def __init__(self, ):
        self.base_url = BASE_URL
        self.headers = HEADERS

    def post(self,endpoint,payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.headers)

    def put(self, endpoint, payload, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=payload, headers= headers or self.headers)
        return response

    def patch(self, endpoint, payload, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.patch(url, json=payload, headers=headers or self.headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers= headers or self.headers)
        return response