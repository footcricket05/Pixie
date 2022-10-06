#Play
from urllib.parse import quote
from requests import get
try:
    from bs4 import BeautifulSoup
except:
    print("Please install bs4!")
def Play(speech):
    if speech.endswith("on YouTube"):
        searchTerm = speech.split()[1:]
        response = get("https://www.youtube.com/results?search_query=" + quote(" ".join(searchTerm[:-2])))
        soup = BeautifulSoup(response.text, "html.parser")
        videos = soup.findAll(attrs={"class":"yt-uix-tile-link"})[1:4]
        #Was [:3], changed to [1:4] to try to stop ads
        #Try to remove google ads if possible (May have fixed, but test this)
        names = list()
        links = list()
        for i in range(len(videos)):
            names.insert(i, videos[i]["title"])
            links.insert(i, "https://www.youtube.com" + videos[i]["href"])
        return("I found 3 videos. " + ". ".join(names), links)

#Search
from webbrowser import open
def Search(speech):
    searchTerm = speech.split()[2:]
    if speech.endswith("online"):
        open("https://www.google.com/search?q=" + quote(" ".join(searchTerm[:-1])))
        return("Searching for " + " ".join(searchTerm))
    elif speech.endswith("on YouTube"):
        return(Play(speech[6:]))
