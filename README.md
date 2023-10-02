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
start - Start working with the bot
select_ai - Select AI
my_id - Get your ID
```
Save the list of commands, replacing the previous list.

### Creating a handler file using the decorator method
###### decorator - @router.<event_type>(<filters, ...>)
To create a handler file similar to `client.py`:

Inside the `handlers` directory, in the `__init__.py` file, write:

`from handlers import other`

In the new file `other.py`:

```
from aiogram import Router, F
from aiogram.types import Message

other_router = Router()

@other_router.message(F.text == "/dice")
async def cmd_dice(message: Message):
    # Your code here...
    # await message.answer("🎲")

```

In the `main.py` file, import:

`from handlers.other import other_router`

And within the function:
```
async def main():
    dp.include_router(other_router)
    # Your code here...
    await dp.start_polling(bot)
```
Done!

### Creating a handler file using observer method
###### By observer method - router.<event_type>.register(handler, <filters, ...>)

To create a handler file similar to `client.py`

Inside the `handlers`directory, in the `__init__.py` file, write:

`from handlers import client`

In the new file  `client.py`:

```
from aiogram import Router, F
from aiogram.types import Message
from create_bot import bot, admin_id
import keyboards as kb

my_router = Router()

#  creation of an asynchronous function

async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')

# register handler, you can register more

def register_handlers_client():
    my_router.message.register(cmd_my_id, F.text == '/my_id')
    # Your code here...
```

In the `main.py` file, import:

`from handlers.client import my_router, register_handlers_client`

And within the function:
```
async def main():
    register_handlers_client()
    dp.include_router(my_router)
    pass ...
    await dp.start_polling(bot)
```
Done!

TEST COMMIT -S -m in IDE
