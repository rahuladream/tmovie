# Python core import

import logging
import os
from queue import Queue
from threading import Thread
from time import time
import requests
import re
from bs4 import BeautifulSoup


# Basic logging to get more detailed information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MovieScrapper(Thread):
    def __init__(self, queue):
        self.queue = queue
    

    def run(self):
        while True:
            # get the work done tha data and work done mutliply
            tr = self.queue.get()
            try:
                movie_string           = tr.find('td',{'class':'titleColumn'}).text
                movie_title            = movie_string.split('\n')[2].strip()
                movie_year             = re.search('\((.*?)\)', movie_string.split('\n')[3].strip()).group(1)
                movie_rating           = tr.find('td', {'class': 'ratingColumn imdbRating'}).text
                movie_img_src          = tr.find_all('img')[0]['src']
                movie_link             = tr.find_all('a')[0].get('href')
                movie_uniqueid         = tr.find_all('a')[0].get('href').split('/')[2]

                # Fetching detail page info
                # Basically transferring the route to individual page 
                # and getting more information from there
                
                detail_page_url         = 'https://www.imdb.com' + movie_link
                response_page           = requests.get(detail_page_url)
                fetch_detail_page_info  = BeautifulSoup(response_page.text, 'lxml')
                movie_story_line        = fetch_detail_page_info.find('div', {'class': 'inline canwrap'}).text.split('\n')[2].strip()
                more_info_block         = fetch_detail_page_info.findAll('div', {'class': 'txt-block'})

                # Decide to store the random information into dictionary
                # fetch the information as required

                data_store_dict = {}

                for i in range(0, more_info_block.__len__()):
                    try:
                        txt_info[more_info_block[i].text.split('\n')[1].strip()] = more_info_block[i].text.split('\n')[2].strip()
                    except:
                        # We leave the detail that were missing in the page
                        continue

            finally:
                self.queue.task_done()
