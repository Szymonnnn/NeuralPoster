import tweepy

API_Key = "" #Deleted for github
API_Key_Secret = "" #Deleted for github
Acces_Token = "" #Deleted for github
Acces_Token_Secret = "" #Deleted for github

class Scrap:
    def __init__(self) -> None:
        pass

    def scrap(self, tag_name):
        auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
        auth.set_access_token(Acces_Token, Acces_Token_Secret)

        api = tweepy.API(auth)

        keywords = tag_name
        limit=5

        tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)

        # tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

        # create DataFrame
        columns = ['User', 'Tweet']
        data = []

        for tweet in tweets:
            data.append([tweet.user.screen_name, tweet.full_text])

        #df = pd.DataFrame(data, columns=columns)

        outcome = data[0][1] + "/n" + data[1][1] + "/n" + data[2][1] + "/n" + data[3][1] + "/n" + data[4][1]

        return outcome