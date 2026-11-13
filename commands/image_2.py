def register(bot):
    @bot.message_handler(commands=['image_2'])
    def image_2_command(message):
        bot.reply_to(message, "🖼️ Get Image_2, Change Image_2[span_12](start_span)[span_12](end_span)")
