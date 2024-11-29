from cProfile import label

from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_order_info_keyboard(order_id, lang, status=None):
    keyboard = InlineKeyboardBuilder()

    labels = {
        "uz": {
            "accepted": "Zakaz qabul qilindi",
            "preparing": "Tayyorlanyapti",
            "ready": "Tayyor",
            "on_the_way": "Yo'lda",
            "choose_delivery": "Dostavkachi tanlash"
        },
        "ru": {
            "accepted": "Заказ принят",
            "preparing": "Готовится",
            "ready": "Готово",
            "on_the_way": "В пути",
            "choose_delivery": "Выбрать доставщика"
        }
    }

    # Tugmalarni statusga qarab qo'shamiz
    if status is None:
        # Boshlang'ich holat (zakazning holatini yangilash)
        keyboard.button(text="✅  Zakaz qabul qilindi", callback_data=f"order_{order_id}_accepted_{lang}")
    elif status == "accepted":
        # Zakaz qabul qilindi holati
        keyboard.button(text="🍳 Tayyorlanyapti", callback_data=f"order_{order_id}_preparing_{lang}")
    elif status == "preparing":
        # Tayyorlanyapti holati
        keyboard.button(text="✔️ Tayyor", callback_data=f"order_{order_id}_ready_{lang}")
    elif status == "ready":
        keyboard.button(text="🚛 Dostavkachi tanlash", callback_data=f"order_{order_id}_choose-delivery_{lang}")
    elif status == "on-the-way":
        # Tayyor holati
        keyboard.button(text="🚚 Yo'lda", callback_data=f"order_{order_id}_on-the-way_{lang}")

    keyboard.adjust(2)  # Tugmalarni 2 qatorda joylash
    return keyboard.as_markup()
