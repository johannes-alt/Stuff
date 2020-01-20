import requests 
from bs4 import BeautifulSoup 
import sys


def food_week():
    #webpage with mensa food
    url = 'https://www.swfr.de/essen-trinken/speiseplaene/mensa-institutsviertel/'

    #open with get method
    resp = requests.get(url)

    #http_respone 200 means OK status
    if resp.status_code == 200:
        print('yay there will be food')
        print('The food is:')

        #we need a parser, Python built-in HTML parser is
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e food
        l = soup.find('div',{'id':'speiseplan-tabs'})
        k = l.find('div',{'class':'tab-content'})
        all_days = k.contents
        for i in all_days:
            day = i.findAll('h3')[0].text
            if 'Samstag' in day:
                continue
            print(day)

            for a in i.contents[1:]:
                category = a.find('h4').text
                print('')
                if 'Abendessen' in category:
                    continue
                print(category)
                t = a.find('div').findAll(text=True)
                for i in range(len(t)):
                    l = t[i]
                    if i==0:
                        l = l[4:]
                        while l[0]==' ':
                            l = l[1:]
                    if 'Kennzeichnungen' in l:
                        break
                    print(l)

    else:
        print('No food available')

def food_today():
    #webpage with mensa food
    url = 'https://www.swfr.de/essen-trinken/speiseplaene/mensa-institutsviertel/'

    #open with get method
    resp = requests.get(url)

    #http_respone 200 means OK status
    if resp.status_code == 200:
        print('yay there will be food')

        #we need a parser, Python built-in HTML parser is
        soup = BeautifulSoup(resp.text, 'html.parser')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        l = soup.find('div',{'class':'menu-tagesplan tab-pane fade in show active'})
        
        day = l.findAll('h3')[0].text
        print(day)
        for a in l.contents[1:]:
            category = a.find('h4').text
            print('')
            if 'Abendessen' in category:
                continue
            print(category)
            t = a.find('div').findAll(text=True)
            for i in range(len(t)):
                l = t[i]
                if i==0:
                    l = l[4:]
                    while l[0]==' ':
                        l = l[1:]
                if 'Kennzeichnungen' in l:
                    break
                print(l)



if len(sys.argv)>1:
    if str(sys.argv[1]) == 'today':
        food_today()
    else:
        food_week()
else:
    food_today()
