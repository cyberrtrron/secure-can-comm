# Secure CAN Bus Simulator

## Overview
This project simulates a **Controller Area Network (CAN)** with **secure encrypted communication** between virtual nodes using Python. It allows multiple nodes to send and receive encrypted messages via a simulated CAN bus. The messages are encrypted using **AES encryption** to ensure confidentiality, and integrity checks can be added optionally.

The project also provides a **graphical user interface (GUI)** to interact with the system, allowing users to send and receive encrypted messages between nodes.

## Features
- **Simulated CAN Bus**: Virtual message exchange between nodes.
- **AES Encryption**: Secure message encryption and decryption.
- **Multi-node support**: Multiple nodes (up to 3 in this version) can communicate.
- **Real-time Logs**: Monitor message exchanges in the log.
- **GUI Interface**: Tkinter-based graphical interface to select nodes and send/receive messages.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-can-simulator.git
cd secure-can-simulator
