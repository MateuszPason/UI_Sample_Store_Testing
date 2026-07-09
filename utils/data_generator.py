import uuid
import json
from config.paths import DATA_DIR

def generate_new_user_data() -> dict:
    with open(DATA_DIR / "users.json") as f:
        static_user_data = json.load(f)["register"]

    uid = uuid.uuid4().hex[:8]
    return {
        **static_user_data,
        "name": f"TestUser{uid}",
        "email": f"testemail_{uid}@testemail.com"
    }

def get_correct_login_data() -> dict:
    with open(DATA_DIR / "users.json") as f:
        return json.load(f)["correct_login_data"]

def get_form_data() -> dict:
    with open(DATA_DIR / "form.json") as f:
        return json.load(f)["contact_us"]