def register(bot):
    @bot.message_handler(commands=['date_birth'])
    def date_birth_command(message):
        bot.reply_to(message, "📅 Check Birth Year, Change Birth Year[span_3](start_span)[span_3](end_span)")
