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
    conversation_text = tk.Text(root, state='disabled') # set to disabled so the user can't edit the conversation
    conversation_text.grid(column=0, row=1, sticky='ew')

    # Create a chat box for the message to send
    message_entry = tk.Entry(root)
    message_entry.grid(column=0, row=2, sticky='ew')

    # Create a button to send the message, ttk used to match style of other elements
    send_button = ttk.Button(root, text="Send", command=lambda: [threading.Thread(target=init_ai, args=(message_entry.get(), language_dropdown.get(), conversation_text)).start(), message_entry.delete(0, 'end')]) # run in a seperate thread to prevent gui from freezing
    send_button.grid(column=0, row=3, sticky='ew')

    # Run the GUI
    root.mainloop()

def init_ai(msg, lang, conversation_text):
    load_dotenv()
    api_key = os.getenv('OAI_key')
    client = OpenAI(api_key = api_key)
    main_msg = "Translate the following text into " + lang + " : " + msg
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'system', 'content': 'You are a helpful translator. Reply only with the direct translation of the provided text. Do not add any additional information or context.'},
                  {'role': 'user', 'content': main_msg}
                  ]
    )
    moderation_response = client.moderations.create(input=response.choices[0].message.content)
    moderation_output = moderation_response.results[0]
    conversation_text.config(state='normal') # enable the text box so we can insert to it
    if moderation_output.flagged:
        conversation_text.insert(tk.END, "Your message was flagged\n")
    else:
        conversation_text.insert(tk.END, "You : " + msg + "\n")
        conversation_text.after(0, lambda: conversation_text.insert(tk.END, "Assistant : " + response.choices[0].message.content + "\n"))
    conversation_text.after(0, lambda: conversation_text.config(state='disabled')) # disable the text box so the user can't edit the conversation
        
def main():
    gui_main()

if __name__ == "__main__":
    main()
