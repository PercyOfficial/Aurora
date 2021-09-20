import asyncio
import os
import random
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from DewmiBot.config import get_str_key
from DewmiBot import pbot


plugin_category = "utils"

CARBONLANG = "auto"


@pbot.on_message(filters.command(["carbon"]))

    info={
        "header": "Carbon generators for given text (Fixed style)",
        "usage": [
            "carbon <text>",
            "carbon <reply to text>",
        ],
    },

async def carbon_api(event):
    """A Wrapper for carbon.now.sh"""
    await event.edit("`Processing..`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await event.get_reply_message()
    pcode = event.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)
    cat = await edit_or_reply(event, "`Carbonizing...\n25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await cat.edit("`Be Patient...\n50%`")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

    await cat.edit("`Processing..\n75%`")

    await asyncio.sleep(2)
    await cat.edit("`Done  Done...\n100%`")
    file = "./carbon.png"
    await cat.edit("`Uploading..`")
    await event.client.send_file(
        event.chat_id,
        file,
        caption="Here's your carbon",
        force_document=True,
        reply_to=event.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()

    await cat.delete()

