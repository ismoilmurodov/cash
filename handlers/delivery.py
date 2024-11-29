from aiogram import Router, types
from aiogram.filters import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.delivery_info import delivery_info
from data.orders import orders
from keyboards.orders_keyboard import get_order_info_keyboard

router = Router()


@router.callback_query(lambda call: call.data.startswith("delivery_"))
async def handle_delivery_selection(callback: types.CallbackQuery):
    data = callback.data.split("_")
    delivery_id = int(data[1])
    lang = data[2]

    # Dostavkachi ma'lumotlarini olish
    delivery = next((d for d in delivery_info if d["id"] == delivery_id), None)

    if not delivery:
        await callback.answer("Dostavkachi topilmadi.")
        return

    labels = {
        "uz": "Dostavkachi ma'lumotlari:\n\n",
        "ru": "Информация о доставщике:\n\n"
    }
    response = labels[lang]
    response += (
        f"Dostavkachi / Доставщик: {delivery['name']}\n"
        f"Telefon / Телефон: {delivery['number']}\n"
    )

    # Orqaga tugmasi
    back_button = InlineKeyboardBuilder()
    back_button.button(text="Orqaga / Назад", callback_data=f"back_to_order_{lang}")
    back_button.adjust(1)

    await callback.message.answer(response, reply_markup=back_button.as_markup())
    await callback.answer()


@router.callback_query(lambda call: call.data.startswith("back_to_order_"))
async def back_to_order(callback: types.CallbackQuery):
    lang = callback.data.split("_")[2]
    # Zakaz holatini va tugmalarni qayta chiqaramiz
    order_id = callback.message.reply_markup.inline_keyboard[0][0].callback_data.split("_")[1]
    order = next((order for order in orders if order["order_id"] == int(order_id)), None)
    keyboard = get_order_info_keyboard(order_id, lang, status=order["status"])
    await callback.message.answer("Zakaz ma'lumotlari:", reply_markup=keyboard)
    await callback.answer()
