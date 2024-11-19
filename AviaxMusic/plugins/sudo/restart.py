from pyrogram import filters
from AviaxMusic import app
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.decorators.language import language


@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & SUDOERS)
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text(_["server_1"])


