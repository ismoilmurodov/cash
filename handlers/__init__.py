from aiogram import Router

from .delivery import router as delivery_router
from .language import router as language_router
from .order_info import router as order_info_router
from .start import router as start_router


def cash_handlers(dp:Router):
    dp.include_router(delivery_router)
    dp.include_router(language_router)
    dp.include_router(order_info_router)
    dp.include_router(start_router)