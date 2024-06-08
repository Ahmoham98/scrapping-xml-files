#Third we need to scrap html data's from stocktwit website
import requests
from bs4 import BeautifulSoup

#Defining a class
class HtmlScrapper :
    #initial method
    def __init__(self) :
        pass
    #Defining a method for html scrapping process
    def html_scraper (self):
        #Setting url and header
        url = 'stocktwits.com'
        #Sending request and creating an object from BeautifulSoup class
        header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        request = requests.get (url, headers=header)
        soup = BeautifulSoup(request.text, 'html.parser')
        #finding wanted data in the consideration of the page Html code tags
        total = ["<h1>This is the header</h1>"]
        for dataset in soup.find_all ():
            text = dataset.find ('a').text
            views = dataset.find ('snap').text
            increment = f"<p>{text} --- {views}</p>"
            total.append(increment)
        #Create a file as output
        with open ('Name & View.html', 'a') as file:
            for t in total :
                file.write (t + '\n')


