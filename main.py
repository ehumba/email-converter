import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from formats import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("Email Converter")
        self.root.geometry(f"{self.width}x{self.height}+150+100")
    
    def create_widgets(self):
        # Choose a format
        label_select_format = ttk.Label(self.root, text="Select an email format:", font=("arial", 14))
        label_select_format.pack(padx=5, pady=5)

        selected_format = tk.StringVar()
        select_format = ttk.Combobox(self.root, textvariable=selected_format)
        select_format['values'] = supported_formats
        select_format['state'] = 'readonly'
        select_format.pack(padx=5, pady=5)
        
        # Enter the domain
        label_enter_domain = ttk.Label(self.root, text="Enter the domain:", font=("arial", 14))
        label_enter_domain.pack(padx=5, pady=5)

        domain_input = tk.StringVar()
        domain_entry = ttk.Entry(self.root, textvariable=domain_input)
        domain_entry.pack(padx=5, pady=5)

        # Copy names
        label_names = ttk.Label(self.root, text="Copy name list:", font=("arial", 14))
        label_names.pack(padx=5, pady=5)

        name_input = ScrolledText(self.root, width=25, height=20)
        name_input.pack(padx=5, pady=5)

        # Convert
        convert_button = ttk.Button(self.root, text="Convert")
        convert_button.pack(anchor=tk.SE)



def main():
    # Create the window
    win = Window(800, 550)
    win.create_widgets()
    win.root.mainloop()

main()    