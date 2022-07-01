import telebot
import yaml
import time
import load_data


params = yaml.safe_load(open('config.yaml'))[0]

token = params['telegram_bot']['token']
num_def =  params['load_definitions']['num_def']
site = params['load_definitions']['site']
from_lang = params['load_definitions']['from_lang']
to_lang = params['load_definitions']['to_lang']

bot = telebot.TeleBot(token, threaded = False)

#start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, params['telegram_bot']['start'])

#help command
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, params['telegram_bot']['help'])


@bot.message_handler(content_types=["text"])
def any_msg(message):
    
    word = message.text
    ddl = load_data.DataLoader(word, site, num_def, from_lang, to_lang)
    out = ddl.out()
    
    try:
        bot.send_message(message.chat.id, out)
    except Exception:
        bot.send_message(message.chat.id, "Can't find the word, try again!")


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print('Error', e)
            time.sleep(15)
