from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒Buyurtma berish", callback_data="buyurtma")],
    [InlineKeyboardButton(text="ℹ️Biz haqimizda", callback_data="biz"), InlineKeyboardButton(text="🛍Buyurtmalarim", callback_data="buyurtmalar")],
    [InlineKeyboardButton(text="🏘Filiallar", callback_data="filiallar")],
    [InlineKeyboardButton(text="✍️Fikr bilrdirish", callback_data="fikr"), InlineKeyboardButton(text="⚙️Sozlamalar", callback_data="sozlama")]
    ]
)