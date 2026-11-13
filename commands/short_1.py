def register(bot):
    @bot.message_handler(commands=['short_1'])
    def short_1_command(message):
        bot.reply_to(message, "▶️ Get Short_1, Change Short_1[span_8](start_span)[span_8](end_span)")
