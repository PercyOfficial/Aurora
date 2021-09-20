import os
from pyrogram import Client, filters
from pyrogram.types import *

from DewmiBot.config import get_str_key
from DewmiBot import pbot

TEXT = " Inline button "

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Alive", switch_inline_query="alive"),
        InlineKeyboardButton("Youtube", switch_inline_query="yt"),
        InlineKeyboardButton("tr", switch_inline_query="tr"),
        InlineKeyboardButton("modapk", switch_inline_query="modapk")
        ],[
        InlineKeyboardButton("ud", switch_inline_query="ud"),
        InlineKeyboardButton("google", switch_inline_query="google"),
        InlineKeyboardButton("webss", switch_inline_query="webss"),
        InlineKeyboardButton("bitly", switch_inline_query="bitly")
        ],[
        InlineKeyboardButton("wall", switch_inline_query="wall"),
        InlineKeyboardButton("pic", switch_inline_query="pic"),
        InlineKeyboardButton("saavn", switch_inline_query="saavn"),
        InlineKeyboardButton("deezer", switch_inline_query="deezer")
        ],[
        InlineKeyboardButton("torrent", switch_inline_query="torrent"),
        InlineKeyboardButton("reddit", switch_inline_query="reddit"),
        InlineKeyboardButton("imdb", switch_inline_query="imdb"),
        InlineKeyboardButton("spaminfo", switch_inline_query="spaminfo"),
        ],[
        InlineKeyboardButton("lyrics", switch_inline_query="lyrics"),
        InlineKeyboardButton("paste", switch_inline_query="paste"),
        InlineKeyboardButton("define", switch_inline_query="define"),
        InlineKeyboardButton("synonyms", switch_inline_query="synonyms"),
        ],[
        InlineKeyboardButton("antonyms", switch_inline_query="antonyms"),
        InlineKeyboardButton("country", switch_inline_query="country"),
        InlineKeyboardButton("cs", switch_inline_query="cs"),
        InlineKeyboardButton("fakegen", switch_inline_query="fakegen"),
        ],[
        InlineKeyboardButton("weather", switch_inline_query="weather"),
        InlineKeyboardButton("datetime", switch_inline_query="datetime"),
        InlineKeyboardButton("app", switch_inline_query="app"),
        InlineKeyboardButton("Github", switch_inline_query="gh"),
        ],[
        InlineKeyboardButton("so ", switch_inline_query="so"),
        InlineKeyboardButton("wiki", switch_inline_query="wiki"),
        InlineKeyboardButton("ping", switch_inline_query="ping"),
        InlineKeyboardButton("pokedex", switch_inline_query="pokedex"),
        ]]
    )

@pbot.on_message(filters.command(["inline"]))
async def inline(pbot, update):
    await update.reply_text(
        text=TEXT,    
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
