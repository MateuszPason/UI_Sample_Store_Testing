import uuid
import json
from config.paths import DATA_DIR


def generate_random_uid() -> str:
    return uuid.uuid4().hex[:8]


def generate_new_user_data() -> dict:
    with open(DATA_DIR / "users.json") as f:
        static_user_data = json.load(f)["register"]

    uid = generate_random_uid()
    return {
        **static_user_data,
        "name": f"TestUser{uid}",
        "email": generate_user_email(),
    }


def get_correct_login_data() -> dict:
    with open(DATA_DIR / "users.json") as f:
        return json.load(f)["correct_login_data"]


def get_form_data() -> dict:
    with open(DATA_DIR / "form.json") as f:
        return json.load(f)["contact_us"]


def get_search_data() -> dict:
    with open(DATA_DIR / "search.json") as f:
        return json.load(f)["scenarios"]


def generate_user_email() -> str:
    uid = generate_random_uid()
    return f"testemail_{uid}@testemail.com"


def get_credit_card_details() -> dict:
    with open(DATA_DIR / "card_payment.json") as f:
        return json.load(f)["card_details"]
