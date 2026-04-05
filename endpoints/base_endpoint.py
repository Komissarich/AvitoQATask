from requests import Response


class BaseEndpoint:
    response: Response = None
    response_json: dict | list = None
    base_url: str = 'https://qa-internship.avito.com'


    def check_200(self):
        print( "STATUSCODE", self.response.status_code)
        assert self.response.status_code == 200

    def check_400(self):
        assert self.response.status_code == 400
    
    def check_404(self):
        assert self.response.status_code == 404

    def check_500(self):
        assert self.response.status_code == 500
        
    