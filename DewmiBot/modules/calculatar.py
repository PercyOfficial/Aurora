import os
from pyrogram import Client, filters
from pyrogram.types import *

from DewmiBot.config import get_str_key
from DewmiBot import pbot

CALCULATE_TEXT = "simple calculator\n\n@szrosebot🇱🇰"

CALCULATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("DEL", callback_data="DEL"),
        InlineKeyboardButton("AC", callback_data="AC"),
        InlineKeyboardButton("(", callback_data="("),
        InlineKeyboardButton(")", callback_data=")")
        ],[
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
        InlineKeyboardButton("÷", callback_data="/")
        ],[
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
        InlineKeyboardButton("6", callback_data="6"),
        InlineKeyboardButton("×", callback_data="*")
        ],[
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
        InlineKeyboardButton("-", callback_data="-"),
        ],[
        InlineKeyboardButton(".", callback_data="."),
        InlineKeyboardButton("0", callback_data="0"),
        InlineKeyboardButton("=", callback_data="="),
        InlineKeyboardButton("+", callback_data="+"),
        ]]
    )

@pbot.on_message(filters.command(["calculator"]))
async def calculate(pbot, update):
    await update.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@pbot.on_callback_query()
async def data(bot, update):
        data = update.data
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
        except Exception as error:
            print(error)
        
@pbot.on_inline_query()
async def line(bot, update):  
    if len(update.data) == 0:        
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description=f"New calculator",
                    input_message_content=InputTextMessageContent
            ]
        except Exception as error:
            print(error)
    else:
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            data = message_text.replace("×", "*").replace("÷", "/")
            text = float(eval(data))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {text}",
                        disable_web_page_preview=True
                    )
                )
            ]
        except:
            pass
    await update.answer(answers)
