from aiogram import Router, types
from data.user_data import user_language
from data.orders import orders
from keyboards.orders_keyboard import get_order_info_keyboard

router = Router()


@router.callback_query(lambda call: call.data.startswith("lang_"))
async def handle_language_selection(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lang = callback.data.split("_")[1]  # "uz" yoki "ru"
    user_language[user_id] = lang  # Tilni saqlaymiz

    # Foydalanuvchiga xabar yuborish
    labels = {
        "uz": "Til muvaffaqiyatli tanlandi! Buyurtmalar haqida ma'lumot:\n\n",
        "ru": "Язык успешно выбран! Информация о заказах:\n\n"
    }
    response = labels[lang]
    for order in orders:
        response += (
            f"Order ID: {order['order_id']}\n"
            f"Ismi / Имя: {order['user_info']['name']}\n"
            f"Telefon / Телефон: {order['user_info']['number']}\n"
            f"Manzil / Адрес: {order['user_info']['location'][lang]}\n"
            f"Buyurtma / Заказ: {order['order_info'][lang]}\n"
            f"To'lov holati / Статус оплаты: {order['pay_status'][lang]}\n"
            f"To'lov turi / Тип оплаты: {order['payment_type'][lang]}\n\n"
        )
        await callback.message.answer(response, reply_markup=get_order_info_keyboard(order['order_id'], lang=lang))
        response = ""  # Har bir zakazni alohida chiqarish uchun

    await callback.answer()  # Callback xabarini yo'q qilish
