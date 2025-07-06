import tkinter as tk
from tkinter import ttk
from formats import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("Email Converter")
        self.root.geometry(f"{self.width}x{self.height}+150+100")


def main():
    win = Window(1000, 800)
    label_select_format = ttk.Label(win.root, text="Select an email format:")
    
    
    win.root.mainloop()

main()    