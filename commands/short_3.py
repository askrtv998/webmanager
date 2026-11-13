def register(bot):
    @bot.message_handler(commands=['short_3'])
    def short_3_command(message):
        bot.reply_to(message, "▶️ Get Short_3, Change Short_1[span_10](start_span)[span_10](end_span)")
