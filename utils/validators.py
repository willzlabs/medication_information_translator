import re

def validate_medication_name(name):
    if not name:
        return False

    return bool(re.fullmatch(r"[A-Za-z\s-]+", name))