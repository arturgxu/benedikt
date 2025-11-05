from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Здарова, {message.from_user.first_name}! 👋\n\n"
        "Я — Бенедикт. Судья, философ и тот, кого тебе стоит боятся."
        " Зови, если нужно рассудить спор или навести порядок в чате."
    )