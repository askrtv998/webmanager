def register(bot):
    @bot.message_handler(commands=['passkey'])
    def passkey_command(message):
        bot.reply_to(message, "🔑 Get Your Passkey, Change Passkey[span_1](start_span)[span_1](end_span)")
