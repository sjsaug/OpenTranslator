## OpenTranslator

### About
A GUI-based translator app utilizing a fine-tuned version of the GPT-4 model, written in Python.

### Features
- Precise Results : Utilizes a fine-tuned version of the GPT-4 model for accurate results.
  <br/>Also compatible with other models such as GPT-3.5-turbo (used in this public release).
- Moderation System : Utilizes the OpenAI moderation API to moderate content sent to the model.
  <br/>If content is flagged, user will be met with a warning message.
- Config System : Utilizes configparser to maintain a seamless experience while retrieving information from the config.
  <br/>Config outfitted with Dev options to view debugging information, useful for seeing why a message was flagged.

### Usage
1. Make sure the following dependancies are installed with `pip install` :
    - openai
    - configparser
2. Create a `.env` file containing the following *OAI_KEY = 'YOUR_API_KEY'* (replace YOUR_API_KEY with your OpenAI key
3. That's it! Run `main.py` and the app should launch!
     - Make sure you are in the directory where `ot.cfg` is located, or else the app won't recognize the config!
