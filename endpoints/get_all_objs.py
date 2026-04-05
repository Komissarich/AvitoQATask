from endpoints.base_endpoint import BaseEndpoint

import requests

class GetAllObjects(BaseEndpoint):

    def get_all_objects(self, seller_id):
        self.response = requests.get(f"{self.base_url}/api/1/{seller_id}/item")
        if self.response.status_code == 200:
            try:
                self.response_json = self.response.json()
            except:
                self.response_json = None

    def check_all_objs(self, ids, payload):
        for index in range(len(self.response_json)):
            assert self.response_json[index]['id'] == ids[index]
            assert self.response_json[index]["name"] == payload[index]['name']
            assert self.response_json[index]["price"] == payload[index]['price']
            assert self.response_json[index]["sellerId"] == payload[index]['sellerId']
            assert "statistics" in self.response_json[index]
            assert self.response_json[index]["statistics"]["contacts"] == payload[index]['statistics']["contacts"]
            assert self.response_json[index]["statistics"]["likes"] == payload[index]['statistics']["likes"]
            assert self.response_json[index]["statistics"]["viewCount"] == payload[index]['statistics']["viewCount"]