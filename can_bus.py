# app/can_bus.py

class CANBus:
    def __init__(self):
        self.messages = []
        
    def send(self, message):
        """Simulate sending a message through the CAN bus."""
        print(f"Sending message over CAN Bus: {message}")
        self.messages.append(message)
        
    def receive(self):
        """Simulate receiving a message from the CAN bus."""
        if self.messages:
            message = self.messages.pop(0)
            print(f"Received message from CAN Bus: {message}")
            return message
        return None
