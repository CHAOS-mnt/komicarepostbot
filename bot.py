import configparser
import requests

config = configparser.ConfigParser()
config.read('bot.ini')
token = config.get('Telegram','token')
channel_id = config.get('Telegram','channel_id')

def getLastPostNumber():
    channel_web_url = 'https://tg.i-c-a.su/json/' + channel_id[1:]
    r = requests.get(channel_web_url)
    no = r.json()['messages'][0]['message'][1:7]

    return no
test = getLastPostNumber()
print(test)
'''
bot = telegram.Bot(token=token)
text = bot.get_updates(offset=None, limit=1, timeout=0)[0].channel_post['text'][1:7]
print(text)
'''
if __name__ == '__main__':
    print(getLastPostNumber())