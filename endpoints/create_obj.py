from endpoints.base_endpoint import BaseEndpoint 
import requests

class CreateObj(BaseEndpoint):

    def create_obj(self, payload):
        self.response = requests.post(f"{self.base_url}/api/1/item", json=payload)
        self.response_json = self.response.json()

    