# gui.py

import tkinter as tk
from tkinter import ttk
from node import CANNode
from can_bus import CANBus
from crypto_utils import key
import threading
import time

class CANSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure CAN Bus Simulator")

        self.bus = CANBus()
        self.nodes = {}

        self.setup_gui()
        self.create_nodes()

    def setup_gui(self):
        # Dropdown to select sender
        self.sender_label = ttk.Label(self.root, text="Select Sender Node:")
        self.sender_label.pack()
        self.sender_var = tk.StringVar()
        self.sender_dropdown = ttk.Combobox(self.root, textvariable=self.sender_var, state="readonly")
        self.sender_dropdown.pack()

        # Message Entry
        self.message_label = ttk.Label(self.root, text="Message:")
        self.message_label.pack()
        self.message
