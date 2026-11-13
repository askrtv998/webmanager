def register(bot):
    @bot.message_handler(commands=['withdraw'])
    def withdraw_command(message):
        bot.reply_to(message, "🌐 Go to Withdraw Website[span_14](start_span)[span_14](end_span)")
