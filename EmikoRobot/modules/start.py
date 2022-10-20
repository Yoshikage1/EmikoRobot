import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/91ceddb6385938a68637b.mp4"

@register(pattern=("/start"))
async def start(event):
  Text = f"""
*ᴋᴏɴɪᴄʜɪᴡᴀ! {}!*
۞ ɪᴍ ᴋʏᴏᴜᴋᴏ ʜᴏʀɪ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ ɪɴʙᴜɪʟᴛ ᴠᴄ ᴘʟᴀʏᴇʀ. [👋](https://telegra.ph/file/ace3cc2757f843ff71330.jpg)
───────────────────────
× Owner - [Rishav](https://t.me/Lieutenantowner)
× Network - [Dragons Network](https://t.me/dragonsxnetwork)
───────────────────────
۞ ɪᴍ ʜᴇʀᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢᴄ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛʟʏ!

  BUTTON = [[Button.url("Help", "https://t.me/KaruizawaXbot?start=help"), Button.url("Support", "https://t.me/kurumisuppor")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
