import json
import os
from datetime import datetime

class SearchHistory:
    def __init__(self):
        self.file = "data/history.json"
        os.makedirs("data", exist_ok=True)  # Create data/ if it doesn't exist

    def save_search(self, medication, summary):

        record = {
            "drug": medication,
            "summary": summary,
            "time": str(datetime.now())
        }

        if os.path.exists(self.file):

            try:
                with open(self.file, "r") as f:
                    history = json.load(f)
            except json.JSONDecodeError:
                history = []

        else:
            
            history = []

        history.append(record)

        with open(self.file, "w") as f:
            json.dump(history, f, indent=4)

    def get_history(self):

        if not os.path.exists(self.file):
            return []

        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
        
    def clear_history(self):

        if os.path.exists(self.file):
            os.remove(self.file)