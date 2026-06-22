from models.medication import Medication
from utils.validators import validate_medication_name
import requests

class FDAClient:
    def __init__(self):
        self.base_url = "https://api.fda.gov/drug/label.json"

    def fetch_drug_info(self, drug_name):

        if not validate_medication_name(drug_name):
            return None
        
        params = {
            "search": f"openfda.generic_name:{drug_name}", 
            "limit": 1
        }

        try:
            response = requests.get(self.base_url, params=params)

            response.raise_for_status()

            data = response.json()

            if not data.get("results"):
                return None

            return self.create_medication(data)
        
        except requests.exceptions.RequestException:
            return None
        
    def create_medication(self, data):
        result = data["results"][0]

        name = result["openfda"]["generic_name"][0]
        usage = result.get("indications_and_usage", ["Not available"])[0]
        warnings = result.get("warnings", ["Not available"])[0]
        side_effects = result.get("adverse_reactions", ["Not available"])[0]
        instructions = result.get("dosage_and_administration", ["Not available"])[0]

        medication = Medication(name, usage, warnings, side_effects, instructions)

        return medication