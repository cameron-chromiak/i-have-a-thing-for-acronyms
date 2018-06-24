#cameron chromiak
#june 23 2018
#web scraper takes lyrics from azlyrics.com via hard code then does stuff w them
from bs4 import BeautifulSoup
import urllib.request

def stripLyrics(findDivs): 
    findDivs = findDivs.text
    print(findDivs)
    

def parseLyrics(sourceCode):
    soup = BeautifulSoup(sourceCode, 'lxml')
    #print("XXXXXXXXXXXXXXXXXXXXXXXXX \n",soup)
    findDivs = soup.findAll("div")
    #print(findDivs)
    findDivs = findDivs[21]
    stripLyrics(findDivs)     


# 
def getLyrics():
    getRequest = "https://www.azlyrics.com/lyrics/johnmayer/vultures.html"
    response = urllib.request.urlopen(getRequest)
    bytes = response.read()
    sourceCode = bytes.decode()
    #print(sourceCode)
    parseLyrics(sourceCode)

##def songInfo: waiting for implementation 
##    getTitle = input(" ")
##    getArtist = input(" ")
##    searchAzlyrics(getTitle, getArtist)
    
getLyrics()



#https://www.azlyrics.com/lyrics/johnmayer/vultures.html
#https://www.azlyrics.com/lyrics/1975/somebodyelse.html
##    getBreaks = soup.findAll("b")
##    print(getBreaks[1]) returns title
## div 21 is the one w lyrics
## most print statements were for testing
