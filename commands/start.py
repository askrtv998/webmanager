import os

def register(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        banner_path = "logo.png"
        
        # ইউজার ইন্টারফেসে দেখানোর জন্য টেক্সট ও কমান্ড লিস্ট
        help_text = (
            " Use the commands to access the bot \n\n"
            "*Settings -*\n"
            "1) /myaccount - Check Your Account Status[span_2](start_span)[span_2](end_span)\n"
            "2) /signup - Create Your Account[span_3](start_span)[span_3](end_span)\n"
            "3) /login - Login on Server to Access and Use App[span_4](start_span)[span_4](end_span)\n\n"
            "*Security -*\n"
            "4) /email - Check Your email, Change Email[span_5](start_span)[span_5](end_span)\n"
            "5) /passkey - Get Your Passkey, Change Passkey[span_6](start_span)[span_6](end_span)\n\n"
            "*Personal Details -*\n"
            "6) /username - Get Username, Change Username[span_7](start_span)[span_7](end_span)\n"
            "7) /date_birth - Check Birth Year, Change Birth Year[span_8](start_span)[span_8](end_span)\n"
            "8) /gender - Check Gender Status, Change Gender Status[span_9](start_span)[span_9](end_span)\n"
            "9) /call_coin - Get Call Rate per Minute, Change Call Rate[span_10](start_span)[span_10](end_span)\n\n"
            "*Avatar -*\n"
            "10) /profile_photo - Get Profile Photo, Change Profile Photo[span_11](start_span)[span_11](end_span)\n"
            "11) /banner_photo - Get Banner Photo, Change Banner Photo[span_12](start_span)[span_12](end_span)\n\n"
            "*Social Shorts -*\n"
            "12) /short_1 - Get Short_1, Change Short_1[span_13](start_span)[span_13](end_span)\n"
            "13) /short_2 - Get Short_2, Change Short_1[span_14](start_span)[span_14](end_span)\n"
            "14) /short_3 - Get Short_3, Change Short_1[span_15](start_span)[span_15](end_span)\n\n"
            "*Social Images -*\n"
            "15) /image_1 - Get Image_1, Change Image_1[span_16](start_span)[span_16](end_span)\n"
            "16) /image_2 - Get Image_2, Change Image_2[span_17](start_span)[span_17](end_span)\n"
            "17) /image_3 - Get Image_3, Change Image_3[span_18](start_span)[span_18](end_span)\n\n"
            "*Helper Website -*\n"
            "18) /withdraw - Go to Withdraw Website[span_19](start_span)[span_19](end_span)\n"
            "19) /recharge - Go to Reachage Website[span_20](start_span)[span_20](end_span)"
        )

        # যদি logo.png ফাইলটি ফোল্ডারে থাকে তবে ব্যানারসহ সেন্ড করবে, না থাকলে শুধু টেক্সট পাঠাবে
        if os.path.exists(banner_path):
            with open(banner_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=help_text, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, help_text, parse_mode="Markdown")
