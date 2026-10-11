import os, threading, telebot, requests
from flask import Flask

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8352814521:AAEqZ_YsAB9e9qlSWHqKnuuvsfyAdLlEDrk")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running 24/7!"

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "🔥 GOLD Bot Online 24/7! /gold bhejo")

@bot.message_handler(commands=['gold'])
def gold_price(m):
    try:
        r = requests.get("https://api.gold-api.com/price/XAU", timeout=10).json()
        price = r.get('price', 'N/A')
        bot.reply_to(m, f"📈 GOLD: ${price}")
    except Exception as e:
        bot.reply_to(m, f"Error: {e}")

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
