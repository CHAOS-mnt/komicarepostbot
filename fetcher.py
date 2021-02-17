import requests
import logging
from util import htmlTagsToText

class Komica:

    def __init__(self, link):
        self.url = link
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_post(self):
        self.logger.info('Fetching contents')
        try:
            r = requests.get(self.url)
            self.logger.debug('HTTPStatusCode: %s', r.status_code)
            if r.status_code == 200:
                self.logger.debug(r.json()['posts'])
                self.Context = r.json()['posts']
        except:
            self.logger.error('Failed to fetch contents')


if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

    k = Komica('https://majeur.zawarudo.org/virtuelles/res/613265.json')
    k.get_post()