def register(bot):
    @bot.message_handler(commands=['image_3'])
    def image_3_command(message):
        bot.reply_to(message, "🖼️ Get Image_3, Change Image_3[span_13](start_span)[span_13](end_span)")
