import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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

        self.selected_format = tk.StringVar()
        select_format = ttk.Combobox(self.root, textvariable=self.selected_format)
        select_format['values'] = supported_formats
        select_format['state'] = 'readonly'
        select_format.pack(padx=5, pady=5)
        
        # Enter the domain
        label_enter_domain = ttk.Label(self.root, text="Enter the domain:", font=("arial", 14))
        label_enter_domain.pack(padx=5, pady=5)

        self.domain_input = tk.StringVar()
        domain_entry = ttk.Entry(self.root, textvariable=self.domain_input)
        domain_entry.pack(padx=5, pady=5)

        # Copy names
        label_names = ttk.Label(self.root, text="Copy name list:", font=("arial", 14))
        label_names.pack(padx=5, pady=5)

        self.name_input = ScrolledText(self.root, width=25, height=20)
        self.name_input.pack(padx=5, pady=5)

        # Convert
        convert_button = ttk.Button(self.root, text="Convert", command=self.output_window)
        convert_button.pack(anchor=tk.SE)

    def output_window(self):
        # Get the values from the root window
        names = self.name_input.get('1.0', tk.END).strip()
        chosen_format = self.selected_format.get()
        domain = self.domain_input.get().strip()

        # Handle errors and call generator function
        if not names or not domain or not chosen_format:
            tk.messagebox.showerror("Missing Input", "Please fill in all fields.")
            return
        try:
            email_output = generate_emails(names, chosen_format, domain)
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))
            return
        
        # Create an output window called by the Convert button
        out_win = tk.Toplevel(self.root)
        out_win.title("Email Converter Output")
        out_win.geometry("700x500+150+100")

        # Add the textbox with the output
        output_label = ttk.Label(out_win, text="Email address list", font=("arial", 14))
        output_label.pack(padx=5, pady=5)

        output = ScrolledText(out_win, width=40, height=40)
        output.pack(padx=5, pady=5)
        output.insert("1.0", email_output)

        out_win.mainloop()






def main():
    win = Window(800, 550)
    win.create_widgets()
    win.root.mainloop()

main()    