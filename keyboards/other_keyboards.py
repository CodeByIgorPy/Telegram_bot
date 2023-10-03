from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

game_kb = [
    [KeyboardButton(text='🎲'),
     KeyboardButton(text='🎯'),
     KeyboardButton(text='🏀'),
     KeyboardButton(text='⚽'),
     KeyboardButton(text='🎳'),
     KeyboardButton(text='🎰')]]

game = ReplyKeyboardMarkup(keyboard=game_kb,
                           resize_keyboard=True, one_time_keyboard=True,
                           input_field_placeholder='Choose a game')
