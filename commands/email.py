def register(bot):
    @bot.message_handler(commands=['email'])
    def email_command(message):
        bot.reply_to(message, "📧 Check Your email, Change Email")
