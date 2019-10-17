""" It does not do to dwell on dreams and forget to live
Syntax: .time

  © [cHAuHaN](http://t.me/amnd33p)"""

import asyncio
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from uniborg.util import admin_cmd

@borg.on(admin_cmd("time ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    current_time = datetime.now().strftime("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n⚡USERBOT TIMEZONE⚡ \n LOCATION: [cHAuHaN](http://t.me/amnd33p)'s Server \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    reply_msg_id = ""
    if input_str:
        current_time = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = Config.TMP_DOWNLOAD_DIRECTORY + " " + str(datetime.now()) + ".webp"
    img = Image.new("RGBA", (350, 220), color=(0, 0, 0, 115))
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 30)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255))
    img.save(required_file_name)
    if not reply_msg_id == "":
        await borg.send_file(
            event.chat_id,
            required_file_name,
            caption="Userbot: Built by [cHAuHaN](http://t.me/amnd33p)",
            reply_to=reply_msg_id
        )
    else:
        await borg.send_file(
            event.chat_id,
            required_file_name,
            caption="Userbot: Built by [cHAuHaN](http://t.me/amnd33p)",
        )
    os.remove(required_file_name)
    end = datetime.now()
    time_taken_ms = (end - start).seconds
    await event.edit("Created sticker of current time in {} seconds".format(time_taken_ms))
    await asyncio.sleep(5)
    await event.delete()