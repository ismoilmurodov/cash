from aiogram import Router, types
from aiogram.filters import Command
from data.user_data import user_language
from keyboards.language_keyboard import get_language_keyboard

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    user_id = message.from_user.id

    # Faqat bir marta tilni tanlash
    if user_id not in user_language:
        await message.answer(
            "🇺🇿 Tilni tanlang:\n🇷🇺 Выберите язык:",
            reply_markup=get_language_keyboard()
        )
    else:
        await message.answer(
            "Siz allaqachon tilni tanlagansiz. Buyurtmalar haqida ma'lumot olish uchun boshqa buyruqni yuboring.")
