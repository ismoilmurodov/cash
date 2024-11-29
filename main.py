from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from handlers import cash_handlers
from handlers.start import router as start_router
from handlers.language import router as language_router

API_TOKEN = "7010625879:AAFWMiwQ3Dk21KQfaTCb0fgRk8FDXRHtHJ0"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Routerni qo'shamiz
    # dp.include_router(start_router)
    # dp.include_router(language_router)
    cash_handlers(dp)

    # Buyruqlar ro'yxati
    await bot.set_my_commands([
        BotCommand(command="start", description="Botni ishga tushirish")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
