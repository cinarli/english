import uuid

def get_random_key():
    code = str(uuid.uuid4())[:12].replace('-', '').lower()
    return code
