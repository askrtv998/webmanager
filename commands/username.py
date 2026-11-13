def register(bot):
    @bot.message_handler(commands=['username'])
    def username_command(message):
        bot.reply_to(message, "👤 Get Username, Change Username[span_2](start_span)[span_2](end_span)")
