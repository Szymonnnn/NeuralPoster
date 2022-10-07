import tweepy


API_Key = "" #Deleted for github
API_Key_Secret = "" #Deleted for github
Acces_Token = "" #Deleted for github
Acces_Token_Secret = "" #Deleted for github

class Post:
    def __init__(self) -> None:
        pass

    def post(self, text, photo):

        auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
        auth.set_access_token(Acces_Token, Acces_Token_Secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        media = api.media_upload(photo)
        tweet = text
        api.update_status(status=tweet, media_ids=[media.media_id])

    def get_by_user(self, name, amount):
        auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
        auth.set_access_token(Acces_Token, Acces_Token_Secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        tweets = api.user_timeline(screen_name = name, count = amount, tweet_mode = 'extended')
        return tweets
        #to loop it use
        #for tweet in tweets:
        #   print(tweet.full_text)

    def get_by_keywords(self, keywords, amount):
        auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
        auth.set_access_token(Acces_Token, Acces_Token_Secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        tweets = api.search_tweets(q = keywords, count = amount, tweet_mode = 'extended')
        return tweets
        #to loop it use
        #for tweet in tweets:
        #   print(tweet.full_text)

        #to search by hashtag just write hashtag as keywords



#media = api.media_upload("pictures/pic_1.jpg")
#tweet = "Introducing new profile that you can get your daily informations from!"
#post_result = api.update_status(status=tweet, media_ids=[media.media_id])
#tweet = api.update_status("My first tweet!") #Add only text