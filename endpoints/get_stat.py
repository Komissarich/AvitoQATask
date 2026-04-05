from endpoints.base_endpoint import BaseEndpoint 
import requests

class GetStat(BaseEndpoint):

    def get_stat_v1(self, id):
        self.response = requests.get(f"{self.base_url}/api/1/statistic/{id}")
        self.response_json = self.response.json()[0]

    def get_stat_v2(self, id):
        self.response = requests.get(f"{self.base_url}/api/2/statistic/{id}")
        self.response_json = self.response.json()[0]

    def check_stat(self, payload):
        assert self.response_json["contacts"] == payload['statistics']['contacts']
        assert self.response_json["likes"] == payload['statistics']['likes']
        assert self.response_json["viewCount"] == payload['statistics']['viewCount']