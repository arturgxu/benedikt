from aiogram import Router, F
from aiogram.types import Message
from services.openai_api import ask_benedikt
import logging

router = Router()

@router.message(F.text)
async def chat_message(message: Message):
    """
    Regular message handler.
    Responds if the text mentions "Benedikt".
    """

    if not message.text:
        return

    logging.info(f"message received from {message.from_user.username}: {message.text}")

    text = message.text.lower()

    if "бенедикт" in text or "benedikt" in text:
        await message.chat.do("typing")

        response = await ask_benedikt(message.text)
        await message.reply(response)