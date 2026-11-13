def register(bot):
    @bot.message_handler(commands=['gender'])
    def gender_command(message):
        bot.reply_to(message, "⚧ Check Gender Status, Change Gender Status[span_4](start_span)[span_4](end_span)")
