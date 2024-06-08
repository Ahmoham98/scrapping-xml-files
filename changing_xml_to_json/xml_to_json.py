#First we need to scrap the xml files from sahmeto website and then convert them to json file
#Import module requirements
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as E

class xml_to_json :
    
    
    def __init__(self):
        pass

    def scrape (self):
        #url
        url = 'https://sahmeto.com/crypto-sitemap.xml'
        #Setting User_Agent
        header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
        #Parsing data
        request = requests.get (url, headers=header)
        mysoup = BeautifulSoup(request.text, 'xml')
        print (mysoup.find('locs'))
        #Storing xml datas
        xml_data = [mysoup.find_all()]
        #changing xml files to json file's
        tree = E.parse(mysoup)
        root = tree.getroot ()
        d  = []
        for child in root:
            if child.tag not in d :
                d[child.tag] = []
                dic = {}
            for child2 in child:
                if child2.tag not in dic:
                    dic[child2.tag] = child2.text
                    internal_dict = {}
                    for child3 in child2:
                        if child3.tag not in internal_dict:
                            internal_dict[child2.tag] = child3.text
            d[child.tag].appened(dic)
        return d


