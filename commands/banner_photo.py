def register(bot):
    @bot.message_handler(commands=['banner_photo'])
    def banner_photo_command(message):
        bot.reply_to(message, "🖼️ Get Banner Photo, Change Banner Photo[span_7](start_span)[span_7](end_span)")
