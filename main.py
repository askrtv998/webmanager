import os
import telebot
from commands import (
    start, myaccount, signup, login, email, passkey, 
    username, date_birth, gender, call_coin, profile_photo, 
    banner_photo, short_1, short_2, short_3, image_1, 
    image_2, image_3, withdraw, recharge
)

# আপনার টেলিগ্রাম টোকেন
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "9176612733:AAHXgLW4KUr849twomYZPZ2AxSaOHwbOivI")
bot = telebot.TeleBot(TOKEN)

# সব আলাদা ফাইলের কমান্ডগুলো রেজিস্টার করা হচ্ছে
start.register(bot)
myaccount.register(bot)
signup.register(bot)
login.register(bot)
email.register(bot)
passkey.register(bot)
username.register(bot)
date_birth.register(bot)
gender.register(bot)
call_coin.register(bot)
profile_photo.register(bot)
banner_photo.register(bot)
short_1.register(bot)
short_2.register(bot)
short_3.register(bot)
image_1.register(bot)
image_2.register(bot)
image_3.register(bot)
withdraw.register(bot)
recharge.register(bot)

if __name__ == "__main__":
    print("Bot is running with modular structure...")
    bot.infinity_polling()
