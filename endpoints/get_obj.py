from endpoints.base_endpoint import BaseEndpoint 
import requests

class GetObj(BaseEndpoint):

    def get_obj(self, id):
        self.response = requests.get(f"{self.base_url}/api/1/item/{id}")
        self.response_json = self.response.json()[0]

    def check_obj(self, id, payload):
        assert self.response_json['id'] == id
        assert self.response_json["name"] == payload['name']
        assert self.response_json["price"] == payload['price']
        assert self.response_json["sellerId"] == payload['sellerId']
        assert "statistics" in self.response_json
        assert self.response_json["statistics"]["contacts"] == payload['statistics']['contacts']
        assert self.response_json["statistics"]["likes"] == payload['statistics']['likes']
        assert self.response_json["statistics"]["viewCount"] == payload['statistics']['viewCount']

