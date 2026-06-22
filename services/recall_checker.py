import requests

class RecallChecker:
    def __init__(self):
        self.base_url = "https://api.fda.gov/drug/enforcement.json"

    def check_recall(self, drug_name):
        
        try:
            response = requests.get(self.base_url, params={"limit": 100})

            response.raise_for_status()

            data = response.json()

            if not data.get("results"):
                return None
            
            for record in data["results"]:
                product = record.get("product_description", "")

                if drug_name.lower() in product.lower():
                    return {
                        "recall_found": True, 
                        "product": product, 
                        "reason": record.get("reason_for_recall", "Not specified"), 
                        "status": record.get("status", "Unkown"), 
                        "date": record.get("recall_initiation_date", "Unknown")
                    }
                
            return None
        
        except requests.exceptions.RequestException:
            return None