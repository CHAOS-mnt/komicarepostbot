import requests
import time
import logging
import telegram
import configparser
from util import htmlTagsToText

config = configparser.ConfigParser()
config.read('bot.ini')
token = config.get('Telegram','token')
channel_id = config.get('Telegram','channel_id')
new_url = config.get('Program','url')
last_post_no = config.getint('Program','last_post_number')
last_post_position = config.getint('Program','last_post_position')
update_interval = config.getint('Program','update_interval')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = telegram.Bot(token=token)

if last_post_position != 0:
    logging.info('Start in the middle')
else:
    logging.info('Start at the beginning')



class posts:
    def __init__(self, i):
        self.post = Context[i]

    def getPostText(self):
        self.post_text = self.post["com"]
        self.post_text = htmlTagsToText(str(self.post_text))
        return self.post_text

    def getImage(self):
        self.head = "https://majeur.zawarudo.org/virtuelles/src/"
        self.file_name = self.post["tim"] + self.post["ext"]
        self.img_url = self.head + self.file_name
        self.d = requests.get(self.img_url) 
        with open('img/'+self.file_name, 'wb') as img:
            img.write(self.d.content)

    def getEmbedLink(self):
        self.embedlink = htmlTagsToText(str(self.post["embed"]))
        return self.embedlink


def sendImage():
    if 'com' in p.post:
        text = '#' + str(p.post["no"]) + '\n' + htmlTagsToText(str(p.post["com"]))
    else:
        text = '#' + str(p.post["no"])
    if p.post["ext"] == '.jpg' or p.post["ext"] == '.png' or p.post["ext"] == '.jpeg':
        bot.send_photo(chat_id=channel_id, photo=open('img/'+p.file_name, 'rb'), caption=text)
    else:
        bot.send_document(chat_id=channel_id, document=open('img/'+p.file_name, 'rb'))
        bot.send_message(chat_id=channel_id, text=text)

try:
    while True:
        print('-'*20)
        r = requests.get(new_url)
        logging.debug('HTTPStatusCode: %s',r.status_code)
        if r.status_code == 200:
            Context = r.json()["posts"]
        else:
            continue
    
        if last_post_position != 0:
            #查询上次得到的最后回复在新list中的位置 
            for last_post_position in range(1, len(Context)):
                last_post = Context[last_post_position]
                if last_post_no == last_post["no"]:
                    break
                elif last_post_no != last_post["no"] and last_post_position == len(Context) - 1:
                    logging.info('Last post not exist')

        #获取回帖内容
        for last_post_position in range(last_post_position, len(Context)):
            p = posts(last_post_position)
            #判断是否有新回复
            if last_post_no < p.post["no"]:
                config.set('Program','LastPostNumber',str(p.post["no"]))
                with open('bot.ini', 'w') as configfile:
                    config.write(configfile)
                time.sleep(3)
                #分别处理不同类型的回复
                if 'com' in p.post:
                    if 'ext' in p.post:
                        logging.info('Text with Image - NO.' + str(p.post["no"]))
                        p.getImage()
                        text = '#' + str(p.post["no"]) + '\n' + p.getPostText()#无意义
                        sendImage()
                        last_post_no = p.post["no"]
                    elif 'embed' in p.post:
                        logging.info('Text with Youtube Embed - NO.' + str(p.post["no"]))
                        text = p.getPostText()
                        link = p.getEmbedLink()
                        text = '#' + str(p.post["no"]) + '\n' + link + '\n' + text
                        bot.send_message(chat_id=channel_id, text=text)
                        last_post_no = p.post["no"]
                    else:
                        logging.info('Text Only - NO.' + str(p.post["no"]))
                        text = '#' + str(p.post["no"]) + '\n' + p.getPostText()
                        bot.send_message(chat_id=channel_id, text=text)
                        last_post_no = p.post["no"]
                elif 'ext' in p.post:
                    logging.info('Image Only - NO.' + str(p.post["no"]))
                    p.getImage()
                    sendImage()
                    last_post_no = p.post["no"]
                elif 'embed' in p.post:
                    logging.info('Embed Only - NO.' + str(p.post['no']))
                    text = '#' + str(p.post["no"]) + '\n' + p.getEmbedLink()
                    bot.send_message(chat_id=channel_id, text=text)
                    last_post_no = p.post["no"]
            else:
                logging.info('Nothing New')

        time.sleep(update_interval)
finally:
    logging.info('Program Stopped')
    bot.send_message(chat_id=channel_id, text='Bot Offline')