from config.configuration import configuration
from changing_xml_to_json.xml_to_json import xml_to_json
from scapping_coin_names.scrapping_coin_names import coinNameScrapper
from scrapping_html_from_stocktwitts.scrappingHtml import HtmlScrapper


def main ():
    config = configuration ()
    
    choose = None
    while choose != 0 :
        print ("Which of the following you want to start: ")
        print ("0.exit the program")
        print ("1.xml_to_json: This option is going to read sahmeto website xml files and change them to json file for you...")
        print ('2.scrapping_coin_names: This is going to scrap sahmeto website xml files and put the coin names within an array...')
        print ("3.scrappingHtml: By choosing this number, scrapping stocktwit website page starts and create you a file as output that contains that page text and some other information in Html form")
        choose = input ('Which number of the following you need for now? : ')
        if choose == 1 :
            xml_converter = xml_to_json ()
            xml_converter.scrape ()
        elif choose == 2 :
            coin_scraper = coinNameScrapper ()
            coin_scraper.scrpe_coin ()
        elif choose == 3:
            html_scraper = HtmlScrapper ()
            html_scraper.html_scraper ()
        else:
            print ("invalid response... ")
            print ("Enter number 0 to exit program")

if __name__ == '__main__':
    main ()