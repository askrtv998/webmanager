def register(bot):
    @bot.message_handler(commands=['call_coin'])
    def call_coin_command(message):
        bot.reply_to(message, "🪙 Get Call Rate per Minute, Change Call Rate[span_5](start_span)[span_5](end_span)")
