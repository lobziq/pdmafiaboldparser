import requests
import sys
import time
from collections import namedtuple
from bs4 import BeautifulSoup as bs
from helper import BoldParser
import logging
import warnings


def get_page_soup(topic, page):
    return bs(requests.get(topic + '&page={0}'.format(page)).text, 'html.parser')


warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
script, topic, start_page = sys.argv
page = int(start_page) if start_page else 0
last_post_lid = 0
soup = get_page_soup(topic, page)
logging.basicConfig(
    format='%(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(''.join([c for c in soup.title.string if c.isalpha() or c.isdigit()])
                            .rstrip() + '.log', 'w'),
        logging.StreamHandler()
    ])
postparser = BoldParser()

while 1:
    for post_block in soup.find_all('div', {'class', 'post_block'}):
        post_info = post_block.find(class_='ddk33_post_info')
        author = post_info['post-author']
        lid = int(post_block.find(itemprop='replyToUrl').text.replace('#', ''))
        timestamp = post_info['post-date']

        bold_content = ''
        comment_text = post_block.find(itemprop='commentText')
        for br in comment_text.find_all('br'):
            br.extract()
        for post_comment in comment_text.find_all(recursive=False):
            if len(post_comment.attrs.keys()) == 0:
                comment_soup = bs(str(postparser.normalize(str(post_comment))), 'html.parser')
                for bold in comment_soup.find_all('strong', recursive=False):
                    bold_content += bold.text + ' '

        if lid > last_post_lid:
            if len(bold_content) > 0:
                logging.info('{0} ({2}): {1}'
                             .format(author, bold_content, page))
            last_post_lid = lid

    if soup.find('li', {'class': 'next'}):
        page += 1
        # time.sleep(3)  # мож там у ПД антиспам какой, если что можно дилей включить
    else:
        time.sleep(60)

    soup = get_page_soup(topic, page)