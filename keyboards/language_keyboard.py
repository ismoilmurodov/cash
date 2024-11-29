from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_language_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🇺🇿 O'zbekcha", callback_data="lang_uz")
    keyboard.button(text="🇷🇺 Русский", callback_data="lang_ru")
    keyboard.adjust(2)  # Tugmalarni 2 qatorda joylash
    return keyboard.as_markup()
