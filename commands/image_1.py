def register(bot):
    @bot.message_handler(commands=['image_1'])
    def image_1_command(message):
        bot.reply_to(message, "🖼️ Get Image_1, Change Image_1[span_11](start_span)[span_11](end_span)")
