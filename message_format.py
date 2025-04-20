# app/message_format.py

class MessageFormat:
    def __init__(self, data, timestamp=None):
        self.data = data
        self.timestamp = timestamp
        self.format_message()

    def format_message(self):
        """Format the message as a structured format (e.g., JSON or dictionary)."""
        from datetime import datetime
        if not self.timestamp:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.message = {
            'data': self.data,
            'timestamp': self.timestamp
        }
        
    def get_message(self):
        return self.message
