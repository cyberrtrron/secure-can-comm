# node.py
import threading
from crypto_utils import encrypt_message, decrypt_message

class CANNode:
    def __init__(self, name, bus, key):
        self.name = name
        self.bus = bus
        self.key = key

    def send(self, data):
        from crypto_utils import encrypt_message
        encrypted = encrypt_message(data, self.key)
        message = {"sender": self.name, "payload": encrypted}
        self.bus.send(message)

    def decrypt(self, encrypted_data):
        from crypto_utils import decrypt_message
        return decrypt_message(encrypted_data, self.key)

    def listen(self):
        def _listen():
            while True:
                msg = self.bus.receive()
                if msg and msg['sender'] != self.name:
                    decrypted = decrypt_message(msg['payload'], self.key)
                    print(f"[{self.name}] Received from {msg['sender']}: {decrypted}")
        thread = threading.Thread(target=_listen, daemon=True)
        thread.start()
