import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from chatbot.chitchat import ChitChatManager
from chatbot.metar import Metar
from chatbot.weather import Weather
from flask import Flask, request
from chatbot.secret import bot_name, bot_api_key, APP_URL, owm_api_key
app = Flask(__name__)

global bot
global API
chitchat_bot = ChitChatManager()
API = bot_api_key
bot = telegram.Bot(token=API)
dispatcher = Dispatcher(bot, None)

def start(update, context):
    reply = "Hello, I am an assistant bot."
    update.message.reply_text(reply)

def metar(update, context):
    if not context.args:
        update.message.reply_text("You did not provide the ICAO dentifier. Can't retrieve METAR.")
    else:
        metar = Metar(context.args[0])
        reply = metar.get_weather()
        update.message.reply_text(reply)

def weather(update, context):
    weather_keyboard = [[telegram.KeyboardButton('Share current location', request_location=True)]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(weather_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text("Send me your location...", reply_markup=reply_kb_markup);

def get_weather(update, context):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    weather = Weather(owm_api_key)
    data = weather.get_weather(lat, lon)
    if not data:
        update.message.reply_text("Unable to get the weather information.")
    else:
        wind = data["wind"]
        weather_str = "Weather in %s Temperature: %d \u00b0C Condition: %s " % (data["city"], round(data["temp"]), data["condition"])
        weather_str += "Wind %s\u00b0 at %s m/s Pressure: %s inHg Humidity: %s%%" % (wind["deg"], wind["speed"], data["pressure"], data["humidity"])
        update.message.reply_text(weather_str);

def chat(update, context):
    reply = str(chitchat_bot.generate_response(update.message.text))
    update.message.reply_text(reply)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("metar", metar))
dispatcher.add_handler(CommandHandler("weather", weather))
dispatcher.add_handler(MessageHandler(Filters.text, chat))
dispatcher.add_handler(MessageHandler(Filters.location, get_weather))

@app.route(f'/{API}', methods=['POST'])
# response is a JSON object, field OK
def response():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

@app.route('/setWebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook(f'{APP_URL}{API}')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
   return '.'

if __name__ == '__main__':
    app.run(threaded=True)