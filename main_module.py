#pobranie obrazu i tekstu
#f = open("text//text.txt", "r")
#tekst = f.read()


class MainPoster:
    def __init__(self) -> None:
        pass

    def public(self, hasztag):

        #Downloading titles and text of articles from past day till now. It also downloads random photo on this topic
        from news_api import NewsContent
        cont = NewsContent()
        from pathlib import Path
        path_to_file = str(Path(Path.cwd())) + "\pictures\local_filename.jpg"
        text_for_gpt = cont.bring(hasztag, path_to_file)

        from twitter_scraping import Scrap
        scrap = Scrap()
        text_for_gpt = scrap.scrap(hasztag)
        print("TEXT DLA SIECI: \n\n\n" + text_for_gpt)

        #losowanie zmiennych do modelu
        import random
        tensor = random.randint(1, 11)
        iterations = random.randint(10, 70)
        print(tensor)
        print(iterations)

        #Deep dreaming picture and saving ([tensor 1:11], [input name], [iterations of model], [output name])
        from dream_creator import Create
        photo = "pictures//local_filename.jpg"
        creation = Create()
        creation.photo(tensor, photo, iterations, "pictures//pic_deeped.jpg")
        final_photo = "pictures//pic_deeped.jpg"

        #Geting response in human language
        from gpt import Ask
        ask = Ask()
        description = ask.ask(text_for_gpt, 50, 0.9)
        #print("Opis: " + description)
        description = description.replace("\n", " ")
        print("Opis: " + description)
        print("Dlugosc stringa: " + str(len(description + " #" + hasztag)) + " - max 280")

        #Posting on my Twitter acount photo with description
        hasztag = hasztag.replace(" ", "")
        from posting import Post
        post = Post()
        post.post(description + " #" + hasztag, final_photo)


'''
search = Post()
tweets = search.get_by_keywords("#england", 100)
for tweet in tweets:
    print(tweet.full_text)
'''