# main.py
from can_bus import CANBus
from node import CANNode
from crypto_utils import key  # Use same key for both nodes for simplicity

def main():
    bus = CANBus()
    
    node1 = CANNode("Node1", bus, key)
    node2 = CANNode("Node2", bus, key)

    node1.listen()
    node2.listen()

    # Simulate communication
    node1.send("Hello Node2!")
    node2.send("Hi Node1, secured message received!")

if __name__ == "__main__":
    main()
