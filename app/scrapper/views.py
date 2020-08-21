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
        Thread.__init__(self)
        self.queue = queue
    

    def run(self):
        while True:
            # get the work done tha data and work done mutliply
            found_tr = self.queue.get()
            try:
                movie_string           = found_tr.find('td',{'class':'titleColumn'}).text
                movie_title            = movie_string.split('\n')[2].strip()
                movie_year             = re.search('\((.*?)\)', movie_string.split('\n')[3].strip()).group(1)
                movie_rating           = found_tr.find('td', {'class': 'ratingColumn imdbRating'}).text
                movie_img_src          = found_tr.find_all('img')[0]['src']
                movie_link             = found_tr.find_all('a')[0].get('href')
                movie_uniqueid         = found_tr.find_all('a')[0].get('href').split('/')[2]

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
                        data_store_dict[more_info_block[i].text.split('\n')[1].strip()] = more_info_block[i].text.split('\n')[2].strip()
                    except:
                        # We leave the detail that were missing in the page
                        continue
                
                # basically here we create or add the data into the database
                print(data_store_dict)

            finally:
                self.queue.task_done()


def main():
    ts = time()

    url = 'https://www.imdb.com/india/top-rated-indian-movies'
    response_back = requests.get(url)
    scrap_html = BeautifulSoup(response_back.text, 'lxml')
    list_found_tbody = scrap_html.find('tbody', {'class': 'lister-list'})
    found_trs = list_found_tbody.findAll('tr')

    queue = Queue()

    for x in range(8):
        worker = MovieScrapper(queue)
        # setting daemon to true will let the main thread exit
        # even though the wokers are blocking
        worker.daemon = True
        worker.start()
    
    # Put the tasks into the queue as a tuple:
    for found_tr in found_trs[0:1]:
        logging.info('Queueing {}'.format(found_tr.find('td',{'class':'titleColumn'}).text))
        queue.put(found_tr)
    
    queue.join()
    logging.info('Took %s', time() - ts)
