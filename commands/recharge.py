def register(bot):
    @bot.message_handler(commands=['recharge'])
    def recharge_command(message):
        bot.reply_to(message, "🌐 Go to Reachage Website[span_15](start_span)[span_15](end_span)")
