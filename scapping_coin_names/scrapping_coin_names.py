#second, we need to seperate all of the coin names within an array
import requests
from bs4 import BeautifulSoup
#Defining a class
class coinNameScrapper :
    #init method
    def __init__(self):
        pass
    #Defining a method for scrapping the coin names from sahmeto website
    def scrpe_coin (self):
        url = 'https://sahmeto.com/crypto-sitemap.xml'
        header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        request2 = requests.get(url, headers=header)
        mysoup2 = BeautifulSoup(request2.text, 'xml')
        name = []
        for dataset in mysoup2.find_all():
            coin = dataset.find('locs').text
            name.append(coin.split('/')[-1])




