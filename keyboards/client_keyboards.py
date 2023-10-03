from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='Chat GPT-4'),
     KeyboardButton(text='Midjourney')],
    [KeyboardButton(text='links to AI')]]
main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True, one_time_keyboard=True,
                           input_field_placeholder='Choose an option below')

chat_gpt_kb = [
    [KeyboardButton(text='Last chat'),
     KeyboardButton(text='New chat')]]
chat_gpt = ReplyKeyboardMarkup(keyboard=chat_gpt_kb,
                               resize_keyboard=True, one_time_keyboard=True,
                               input_field_placeholder='Choose chat')

links_kb = [
    [InlineKeyboardButton(text='Link to Chat GPT-4', url='https://chat.openai.com/')],
    [InlineKeyboardButton(text='Link to Midjourney', url='https://www.midjourney.com/')]]
links = InlineKeyboardMarkup(inline_keyboard=links_kb)
