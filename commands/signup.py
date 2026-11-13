def register(bot):
    @bot.message_handler(commands=['signup'])
    def signup_command(message):
        bot.reply_to(message, "Use this to Create Your Account.")
