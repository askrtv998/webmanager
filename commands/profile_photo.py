def register(bot):
    @bot.message_handler(commands=['profile_photo'])
    def profile_photo_command(message):
        bot.reply_to(message, "🖼️ Get Profile Photo, Change Profile Photo[span_6](start_span)[span_6](end_span)")
