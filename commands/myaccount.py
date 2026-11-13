def register(bot):
    @bot.message_handler(commands=['myaccount'])
    def myaccount_command(message):
        bot.reply_to(message, "Checking Your Account Status...")
