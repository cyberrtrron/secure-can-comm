# app/main.py
import tkinter as tk
from gui import CANApp

def main():
    root = tk.Tk()
    app = CANApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
