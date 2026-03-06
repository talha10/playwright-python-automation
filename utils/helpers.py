import string
import random
import json

def generate_random_email(domain="test.com"):
    """Generates a random email address."""
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"qa_test_{random_str}@{domain}"

def generate_random_string(length=8):
    """Generates a random alphanumeric string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def read_test_data_from_json(filepath):
    """Reads and parses a JSON file into a Python dictionary."""
    with open(filepath, 'r') as file:
        return json.load(file)
