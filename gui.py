# app/gui.py
import tkinter as tk
from tkinter import messagebox
from can_bus import CANBus
from crypto_utils import CryptoUtils

class CANApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CAN Encryption Application")
        
        # Set up CAN communication and crypto utils
        self.can_bus = CANBus()
        self.crypto_utils = CryptoUtils()

        self.message_label = tk.Label(master, text="Enter message:")
        self.message_label.pack()

        self.message_entry = tk.Entry(master)
        self.message_entry.pack()

        self.send_button = tk.Button(master, text="Send Message", command=self.send_message)
        self.send_button.pack()

        self.receive_button = tk.Button(master, text="Receive Message", command=self.receive_message)
        self.receive_button.pack()

        self.key_label = tk.Label(master, text="Encryption Key:")
        self.key_label.pack()

        self.key_text = tk.Text(master, height=1, width=50)
        self.key_text.pack()
        self.key_text.insert(tk.END, self.crypto_utils.get_key().decode())

    def send_message(self):
        """Encrypt and send the message."""
        message = self.message_entry.get()
        if message:
            encrypted_message = self.crypto_utils.encrypt_message(message)
            self.can_bus.send(encrypted_message)
            messagebox.showinfo("Message Sent", f"Encrypted Message Sent: {encrypted_message}")
        else:
            messagebox.showwarning("Input Error", "Please enter a message.")

    def receive_message(self):
        """Receive and decrypt the message."""
        encrypted_message = self.can_bus.receive()
        if encrypted_message:
            decrypted_message = self.crypto_utils.decrypt_message(encrypted_message)
            messagebox.showinfo("Message Received", f"Decrypted Message: {decrypted_message}")
        else:
            messagebox.showwarning("No Messages", "No messages received.")
