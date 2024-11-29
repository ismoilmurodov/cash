from aiogram import Router, types
from aiogram.filters import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.orders import orders
from keyboards.orders_keyboard import get_order_info_keyboard
from data.delivery_info import delivery_info

router = Router()


@router.callback_query(lambda call: call.data.startswith("order_"))
async def handle_order_status_update(callback: types.CallbackQuery):
    print(callback.data)
    data = callback.data.split("_")
    order_id = int(data[1])
    action = data[2]
    lang = data[3]


    order =     {
        "order_id": "1",
        "user_info": {
            "name": "Ali",
            "number": "+998901234567",
            "location": {"uz": "Toshkent, Yunusobod", "ru": "Ташкент, Юнусабад"}
        },
        "order_info": {
            "uz": "Cola 0.5L - 1 dona, Laqqa baliq - 1.2 kg",
            "ru": "Cola 0.5L - 1 шт., Рыба Лакка - 1.2 кг"
        },
        "pay_status": {"uz": "To'lanmagan", "ru": "Не оплачено"},
        "payment_type": {"uz": "Click", "ru": "Click"},
        "status": "accept"
    }
    print(action)
    # Zakaz holatini yangilash
    if action == "accepted":
        order["status"] = "accepted"
    elif action == "preparing":
        order["status"] = "preparing"
    elif action == "ready":
        order["status"] = "ready"
    elif action == "on-the-way":
        order["status"] = "on-the-way"
    elif action == "choose-delivery":
        # Dostavkachi tanlanishi
        delivery_keyboard = InlineKeyboardBuilder()
        for delivery in delivery_info:
            delivery_keyboard.button(text=delivery["name"], callback_data=f"delivery_{delivery['id']}_{lang}")
        delivery_keyboard.adjust(1)
        await callback.message.answer("Dostavkachi tanlang:", reply_markup=delivery_keyboard.as_markup())
        await callback.answer()
        return

    # Har bir statusga qarab tugmalarni yangilaymiz
    keyboard = get_order_info_keyboard(order_id, lang, status=order["status"])

    # Zakaz haqida ma'lumotlarni chiqarish
    labels = {
        "uz": "Zakaz haqida ma'lumot:\n\n",
        "ru": "Информация о заказе:\n\n"
    }
    response = labels[lang]
    response += (
        f"Order ID: {order['order_id']}\n"
        f"Ismi / Имя: {order['user_info']['name']}\n"
        f"Telefon / Телефон: {order['user_info']['number']}\n"
        f"Manzil / Адрес: {order['user_info']['location'][lang]}\n"
        f"Buyurtma / Заказ: {order['order_info'][lang]}\n"
        f"To'lov holati / Статус оплаты: {order['pay_status'][lang]}\n"
        f"To'lov turi / Тип оплаты: {order['payment_type'][lang]}\n\n"
    )

    await callback.message.edit_reply_markup( reply_markup=keyboard)
    await callback.answer()  # Callbackni to'xtatamiz
