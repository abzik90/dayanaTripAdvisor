from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
browser = webdriver.Chrome("./chromedriver.exe", options=options)

counter=10

def parse(URL):
    global counter

    browser.get(URL)
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    reviews=[]

    reviewSection=soup.find('div',class_='Iwpns')
    reviewCards=str(reviewSection).split('<hr class="cmDEY fBRVc eXrsm"/>')
    print(len(reviewCards))
    for card in reviewCards:
        card=BeautifulSoup(card,'html.parser')
        try:
            reviews.append({
                'author':card.find('a',class_='iPqaD _F G- ddFHE eKwUx btBEK fUpii').get_text(strip=True),#:(authorSpan.find('a',class_="_7c6GgQ6n")).get_text(strip=True),
                'text':card.find('div',class_='WlYyy diXIH dDKKM').find('span').get_text(strip=True),
                'title':card.find('div',class_='WlYyy cPsXC bLFSo cspKb dTqpp').find('span').get_text(strip=True),
                'date':card.find('div',class_='fEDvV').get_text(strip=True)
            })
        except:
            continue    
        print(reviews[-1])
        print("\n")
    print("https://www.tripadvisor.com/"+"Attraction_Review-g294197-d1958940-Reviews-or"+str(counter)+"-Hongik_University_Street-Seoul.html")

    if counter<=1080:
        counter+=10
        parse("https://www.tripadvisor.com/"+"Attraction_Review-g294197-d1958940-Reviews-or"+str(counter)+"-Hongik_University_Street-Seoul.html")

URL="https://www.tripadvisor.com/Attraction_Review-g294197-d1958940-Reviews-Hongik_University_Street-Seoul.html"
parse(URL)
