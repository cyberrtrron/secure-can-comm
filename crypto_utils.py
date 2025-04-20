# app/crypto_utils.py
from cryptography.fernet import Fernet

class CryptoUtils:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_message(self, message):
        """Encrypt a message."""
        encrypted_message = self.cipher.encrypt(message.encode())
        return encrypted_message
    
    def decrypt_message(self, encrypted_message):
        """Decrypt a message."""
        decrypted_message = self.cipher.decrypt(encrypted_message).decode()
        return decrypted_message
        
    def get_key(self):
        """Get the current encryption key."""
        return self.key
