import os
from pyrogram import Client, filters
from pyrogram.types import *

from DewmiBot.config import get_str_key
from DewmiBot import pbot

REPO_TEXT = "**A Powerful and Simple Group Manager Bot To Manage Your Groups Easily ! \n\n↼ Øwñêr ⇀ : 『 PSJ 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Resently\n╰──────────────\n\n»»» @Aurora_x_Bot «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("Repository", url=f"https://github.com/ParkseoJoon2005/Aurora"),
        InlineKeyboardButton("Video info ", url=f"https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA"),
      ],[
        InlineKeyboardButton("𝑺𝒍 𝑩𝒐𝒕 𝒁𝒐𝒏𝒆 ", url="https://t.me/Hermione_Updates"),
        InlineKeyboardButton("𝓢𝓛 𝓑𝓸𝓽 𝓒𝓱𝓪𝓽", url="https://t.me/dihan_official"),
      ],[
        InlineKeyboardButton("Aurora Bot update info", url="https://t.me/HermioneSupport_Official"),
        InlineKeyboardButton("Developer", url="https://t.me/Boy_Alone_In_Universe"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
