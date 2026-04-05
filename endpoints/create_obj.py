from endpoints.base_endpoint import BaseEndpoint 
import requests

class CreateObj(BaseEndpoint):

    def create_obj(self, payload):
        self.response = requests.post(f"{self.base_url}/api/1/item", json=payload)
        try:
            self.response_json = self.response.json()
            print("result", self.response_json)
        except:
            print("Error", self.response.text)

    