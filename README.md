# Learn-French-Bot
Telegram bot which provides information about translation, gender and definitions of french word. Definitions and gender are from [LaRousse site]('https://www.larousse.fr/dictionnaires/francais/').

# Requirements
- `numpy`
- `BeautifulSoup`
- `requests`
- `translate`
- `regex`
- `telebot`
- `yaml`
- `time`

# Files
- **load_data.py**

Python module which loads all needed data, process it and return output.

- **bot.py**

Python module with telegram bot.

- **config.yaml**

File with parameters.

# Usage
1) Create your telegrambot  with @BotFarther;
1) Add token of the the bot to the config file;
2) Launch bot.py
