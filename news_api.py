ApiKey = "" #Deleted for github

from newsapi import NewsApiClient
from datetime import datetime, timedelta
import random
import urllib.request

class NewsContent:
    def __init__(self) -> None:
        pass

    def bring(self, tag, save_path):
        content=""
        newsapi = NewsApiClient(api_key=ApiKey)

        data = newsapi.get_everything(q=tag, language='en', page_size=20, from_param=datetime.today()-timedelta(days=1))

        articles = data['articles']
        #print(data['totalResults'])

        for article in articles:
            content+=article['title']
            content+=" "
            content+=article['content'][0:-17]
            content+=" "
        max = data['totalResults']
        if max>20:
            max=20
        number = random.randint(1, max)
        image_url = articles[number]['urlToImage']
        urllib.request.urlretrieve(image_url, save_path)

        return content


'''
for x, y in enumerate(articles):
    print(f'{x}   {y["title"]}')

for key, value in articles[0].items():
    print(f"\n{key.ljust(15)} {value}")
'''

