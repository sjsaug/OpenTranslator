import tkinter as tk
from tkinter import ttk

def create_gui():
    root = tk.Tk()
    root.title("OpenTranslator")

    # Configure columns to center widgets
    root.columnconfigure(0, weight=1)

    # Create a dropdown menu for language selection
    language_var = tk.StringVar()
    language_dropdown = ttk.Combobox(root, textvariable=language_var)
    language_dropdown['values'] = ('English', 'Spanish', 'French', 'German')  # Add more languages as needed
    language_dropdown.grid(column=0, row=0, sticky='ew')

    # Create a box for the conversation
    conversation_text = tk.Text(root)
    conversation_text.grid(column=0, row=1, sticky='ew')

    # Create a chat box for the message to send
    message_entry = tk.Entry(root)
    message_entry.grid(column=0, row=2, sticky='ew')

    # Run the GUI
    root.mainloop()

def main():
    create_gui()

if __name__ == "__main__":
    main()
