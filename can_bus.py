# can_bus.py
import queue

class CANBus:
    def __init__(self):
        self.message_queue = queue.Queue()

    def send(self, message):
        self.message_queue.put(message)

    def receive(self):
        try:
            return self.message_queue.get(timeout=1)
        except queue.Empty:
            return None
