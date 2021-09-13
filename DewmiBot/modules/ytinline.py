from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery

@Client.on_message(command("youtube") & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🤷‍♂️ bot status:\n"
        f"🙋‍♀️ `PONG!!`\n"
        f"✮✮ **Now online**`{delta_ping * 1000:.3f} ms`\n"
        f"✮✮ **Time Taken:** `{uptime}`\n"
        f"✮✮ **Service uptime:** `{START_TIME_ISO}`",
        reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🔎 Search Youtube",  switch_inline_query_current_chat="")
                       ],
                         
                       ]
                    )
    )
