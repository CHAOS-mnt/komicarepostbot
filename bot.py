from telegram import Bot
import logging

class ForwardBot(Bot):

    def __init__(self, token):
        super().__init__(token=token)
        self.logger =logging.getLogger(self.__class__.__name__)
        self.logger.info('Initializing')

    def send(self, channel_id, text, *file):
        if file:
            if file[0][-3:] == 'jpg' or file[0][-3:] == 'png' or file[0][-3:] == 'jpeg':
                self.logger.info('Picture with Text - NO.'+text[:7])
                self.send_photo(chat_id=channel_id, photo=open('img/' + file[0], 'rb'), caption=text)
            else:
                self.logger.info('File with Text - NO.'+text[:7])
                self.send_document(chat_id=channel_id, document=open('img/' + file[0], 'rb'))
                self.send_message(chat_id=channel_id, text=text)
        else:
            self.logger.info('Text Only - NO.'+text[:7])
            self.send_message(chat_id=channel_id, text=text)

if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

    b=ForwardBot('1065530671:AAHVxJIHTV_QmOhyhqLbBgDvodavWWayivA')

    b.send('@hsuusbagaianayxxyhb', 'testlog')
