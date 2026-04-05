from endpoints.base_endpoint import BaseEndpoint 
import requests

class DeleteObj(BaseEndpoint):

    def del_obj(self, id):
        self.response = requests.delete(f"{self.base_url}/api/2/item/{id}")
        if self.response.status_code == 200:
            try:
                self.response_json = self.response.json()
            except:
                self.response_json = None

