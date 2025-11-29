import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("8317269364:AAGw_SRnaRZKYfP1s7xHUREFLzRK6P3gYzo")

# ---------- MAIN MENU ----------
def main_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    tiktok_btn = InlineKeyboardButton("🎵 TikTok Service", callback_data="tiktok_menu")
    bg_btn = InlineKeyboardButton("🖼 BG Remove", url="https://www.remove.bg/upload")
    channel_btn = InlineKeyboardButton("📢 My Channel", url="https://t.me/sowrovcreate")
    menu.add(tiktok_btn, bg_btn, channel_btn)
    return menu

# ---------- TIKTOK SUB MENU ----------
def tiktok_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    like_btn = InlineKeyboardButton("❤️ Like", url="https://zefoy.com")
    view_btn = InlineKeyboardButton("👁 View", url="https://your-view-link.com")
    comment_btn = InlineKeyboardButton("💬 Comment", url="https://your-comment-link.com")
    back_btn = InlineKeyboardButton("⬅ Back", callback_data="back_main")
    menu.add(like_btn, view_btn, comment_btn, back_btn)
    return menu

# ---------- START COMMAND ----------
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "Welcome! Choose a service:", reply_markup=main_menu())

# ---------- CALLBACK HANDLER ----------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "tiktok_menu":
        bot.edit_message_text(
            "Choose TikTok Service:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=tiktok_menu()
        )
    elif call.data == "back_main":
        bot.edit_message_text(
            "Welcome! Choose a service:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

bot.infinity_polling()
