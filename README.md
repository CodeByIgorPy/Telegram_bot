# Telegram_bot
### Creating a Virtual Environment

1. Open your project in PyCharm.


2. Open the terminal in PyCharm. You can do this by clicking on the "Terminal" tab at the bottom part of the IDE window.


3. Create a virtual environment. You can use the venv module for this. Type the following command into the terminal:

`python -m venv venv`


4. Activate the virtual environment:
- For Windows:

`.\venv\Scripts\activate`


- For macOS and Linux:

`source venv/bin/activate`

Now, you have the virtual environment activated in the PyCharm terminal. Any packages you install using pip will be installed into this virtual environment.


The command pip install -r requirements.txt is used to install Python packages listed in the requirements.txt file. This file is commonly used in Python projects for managing dependencies.

`pip install -r requirements.txt`


### Instructions for adding a command menu:

1. Join the `BotFather` chat.
2. Enter the command `/setcommands`.
3. Choose the desired bot from the provided list.
Provide the list of commands in the following format:
```
start - start working with the bot
my_id - Get your ID
```
Save the list of commands, replacing the previous list.