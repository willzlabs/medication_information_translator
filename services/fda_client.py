import requests

class FDAClient:
    def __init__(self):
        self.base_url = "https://api.fda.gov/drug/label.json"

    def fetch_drug_info(self, drug_name):
        
        params = {
            "search": f"openfda.generic_name:{drug_name}", 
            "limit": 1
        }

        try:
            response = requests.get(self.base_url, params=params)

            response.raise_for_status()

            data = response.json()

            return data
        except requests.exceptions.RequestException:
            return None