# Python core imports
import requests

# Django Core settings
from django.conf import settings

# Async middleware
from django.utils.decorators import sync_and_async_middleware

"""
Handling the error direct app
"""

@sync_and_async_middleware
class StackOverflowMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)
        return response
    

    def process_exception(self, request, exception):

        
        if settings.DEBUG:
            
            # import pdb; pdb.set_trace()

            intitle = u'{}'.format(exception.__class__.__name__)
            
            print(intitle)

            url = 'https://api.stackexchange.com/2.2/search'
            # headers = { 'User-Agent': 'github.com/vitorfs/seot' }
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',
                'intitle': intitle
            }

            r = requests.get(url, params=params)
            questions = r.json()

            for question in questions['items']:
                print (question['title'])
                print (question['link'])
                print ("")

        return None