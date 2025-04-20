# crypto_utils.py
from cryptography.fernet import Fernet

# Generate a key (one-time setup)
# key = Fernet.generate_key()
# print(key.decode())

key = b'your_pre_generated_fernet_key_here'  # Store securely
cipher = Fernet(key)

def encrypt_message(message: str, key=None):
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(token: str, key=None):
    return cipher.decrypt(token.encode()).decode()
