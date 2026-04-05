from endpoints.base_endpoint import BaseEndpoint 
import requests

class DeleteObj(BaseEndpoint):

    def del_obj(self, id):
        self.response = requests.delete(f"{self.base_url}/api/2/item/{id}")
        try:
            self.response_json = self.response.json()
        except:
            pass

