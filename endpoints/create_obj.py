from endpoints.base_endpoint import BaseEndpoint 
import requests

class CreateObj(BaseEndpoint):

    def create_obj(self, payload):
        self.response = requests.post(f"{self.base_url}/api/1/item", json=payload)
        if self.response.status_code == 200:
            try:
                self.response_json = self.response.json()
            except:
                self.response_json = None

    