import tkinter as tk
from tkinter import ttk
from openai import OpenAI
from dotenv import load_dotenv
import os
import threading

def gui_main():
    root = tk.Tk()
    root.title("OpenTranslator")

    # Configure columns to center widgets
    root.columnconfigure(0, weight=1)

    # Create a dropdown menu for language selection
    language_var = tk.StringVar()
    language_dropdown = ttk.Combobox(root, textvariable=language_var, state='readonly')
    language_dropdown['values'] = ('English', 'Spanish', 'French', 'German')  # Add more languages as needed
    language_dropdown.grid(column=0, row=0, sticky='ew')

    # Create a box for the conversation
    conversation_text = tk.Text(root)
    conversation_text.grid(column=0, row=1, sticky='ew')

    # Create a chat box for the message to send
    message_entry = tk.Entry(root)
    message_entry.grid(column=0, row=2, sticky='ew')

    # Create a button to send the message
    send_button = tk.Button(root, text="Send", command=lambda: threading.Thread(target=init_ai, args=(message_entry.get(), language_dropdown.get(), conversation_text)).start())
    send_button.grid(column=0, row=3, sticky='ew')

    # Run the GUI
    root.mainloop()

def init_ai(msg, lang, conversation_text):
    load_dotenv()
    api_key = os.getenv('OAI_key')
    client = OpenAI(api_key = api_key)
    main_msg = "Translate the following message into" + lang + ": " + msg
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful translator. Translate the provided text into the desired language..'},
            {'role': 'user', 'content': main_msg}
        ]
    )
    conversation_text.insert(tk.END, response.choices[0].message.content + "\n")
    

def main():
    gui_main()

if __name__ == "__main__":
    main()
