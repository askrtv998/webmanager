def register(bot):
    @bot.message_handler(commands=['login'])
    def login_command(message):
        bot.reply_to(message, "Login on Server to Access Use App.")
