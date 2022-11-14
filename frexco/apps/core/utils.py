import random
import string

DEFAULT_CHAR_STRING = string.ascii_letters + string.digits + "!@#$%^&*()"

def generate_random_string(chars=DEFAULT_CHAR_STRING, size=6):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_random_password(chars=DEFAULT_CHAR_STRING, size=8):
    return ''.join(random.choice(chars) for _ in range(size))