import configparser
import requests
from bs4 import BeautifulSoup


config = configparser.ConfigParser()
config.read('bot.ini')
token = config.get('Telegram','token')
channel_id = config.get('Telegram','channel_id')


def htmlTagsToText(html_string):
    soup=BeautifulSoup(html_string, features="html.parser")
    refer = soup.find_all('span')
    link = soup.find_all('a')
    div_tag = soup.find_all('div')
    if len(div_tag) != 0:
        for i in range(0, len(div_tag)):
            div = div_tag[i]
            div_a_link = div.find('a')['href']
            div_tag[i].replace_with(div_a_link)
            html_string = str(soup)
    #处理引用回复
    if len(refer) != 0:
        for m in range(0, len(refer)):
            refer[m].replace_with(refer[m].get_text())
            html_string = str(soup)
    #处理a标签
    if len(link) != 0:
        for n in range(0, len(link)):
            if str(link[n]).find('onclick') != -1:
                #print('It/'s Reply')
                reply_target = link[n].get_text()
                link[n].replace_with(reply_target)
                html_string = str(soup)
            else:
                url_source = link[n]['href']
                link[n].replace_with(url_source)
                html_string = str(soup)
    html_string = html_string.replace("&gt;", ">")
    html_string = html_string.replace("&amp;", "&")
    return html_string.replace("<br/>", "\n")


def getLastPostNumber():
    channel_web_url = 'https://tg.i-c-a.su/json/' + channel_id[1:]
    r = requests.get(channel_web_url)
    no = r.json()['messages'][0]['message'][1:7]
    return int(no)