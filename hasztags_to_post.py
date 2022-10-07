#This is the main module
from bs4 import BeautifulSoup
import requests
from main_module import MainPoster

URL = "https://twitter-trends.iamrohit.in/united-states"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("a", class_="tweet")
for result in results:
    tweet_tag = result.text
    if(tweet_tag[0]=="#"):
        tweet_tag = tweet_tag[1:]
    print(tweet_tag)

    try:
        post = MainPoster()
        post.public(tweet_tag)
    except:
        print(tweet_tag + " exception")

#pomyśleć nad dodawaniem linku do tweeta(może to być zły pomysł, bo zwiększy się liczba znaków),
#  braniu tylko kulku pierwszych trejdujących hasztagów
#  i uruchamianiu skryptu co konkretny czas