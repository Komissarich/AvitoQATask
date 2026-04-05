from endpoints.base_endpoint import BaseEndpoint 
import requests

class GetStat(BaseEndpoint):

    def get_stat_v1(self, id):
        self.response = requests.get(f"{self.base_url}/api/1/statistic/{id}")
        self.response_json = self.response.json()

    def get_stat_v2(self, id):
        self.response = requests.get(f"{self.base_url}/api/2/statistic/{id}")
        self.response_json = self.response.json()

    def check_stat(self, payload):
        assert "statistics" in self.response_json
        assert self.response_json["statistics"]["contacts"] == payload['statistics']['contacts']
        assert self.response_json["statistics"]["likes"] == payload['statistics']['likes']
        assert self.response_json["statistics"]["viewCount"] == payload['statistics']['viewCount']