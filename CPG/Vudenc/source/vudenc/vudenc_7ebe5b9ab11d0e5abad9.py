def telegram_send_mess(mess, **kwargs):...
import telebot
from telebot import apihelper
import sql
telegrams = sql.get_telegram_by_ip(kwargs.get('ip'))
proxy = sql.get_setting('proxy')
for telegram in telegrams:
token_bot = telegram[1]
if proxy is not None:
channel_name = telegram[2]
apihelper.proxy = {'https': proxy}
bot = telebot.TeleBot(token=token_bot)
print(
    "Fatal: Can't send message. Add Telegram chanel before use alerting at this servers group"
    )
bot.send_message(chat_id=channel_name, text=mess)
sys.exit()
