def register(bot):
    @bot.message_handler(commands=['short_2'])
    def short_2_command(message):
        bot.reply_to(message, "▶️ Get Short_2, Change Short_1[span_9](start_span)[span_9](end_span)")
