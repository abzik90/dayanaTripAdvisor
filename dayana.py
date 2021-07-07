from selenium import webdriver
from bs4 import BeautifulSoup

counter=10

def parse(page_source):
    global counter
    soup = BeautifulSoup(page_source, 'html.parser')
    reviewSection=soup.find('div',class_='_1c8_1ITO')
    authorSpans=reviewSection.findAll('span',class_='DrjyGw-P _1SRa-qNz _2AAjjcx8')
    textSpans=reviewSection.findAll('span',class_='_2tsgCuqy')
    dateDivs=reviewSection.findAll('div',class_='DrjyGw-P _26S7gyB4 _1z-B2F-n _1dimhEoy')
    nextUrl=reviewSection.find('a',class_='_23XJjgWS _22upaSQN _1hF7hP_9 _2QvUxWyA')
    reviews=[]

    for authorSpan,textSpan,dateDiv in zip(authorSpans,textSpans,dateDivs):
        reviews.append({
            'author':(authorSpan.find('a',class_="_7c6GgQ6n")).get_text(strip=True),
            'text':textSpan.get_text(strip=True),
            'date':dateDiv.get_text(strip=True)
        })


    for review in reviews:
        print(review['author'])
        print(review['text'])
        print(review['date'])
        print("\n")
    print("https://www.tripadvisor.com"+"Attraction_Review-g294197-d1958940-Reviews-or"+str(counter)+"-Hongik_University_Street-Seoul.html")
    browser.get("https://www.tripadvisor.com/"+"Attraction_Review-g294197-d1958940-Reviews-or"+str(counter)+"-Hongik_University_Street-Seoul.html")
    if counter<=1080:
        counter+=10
        parse(browser.page_source)


URL="https://www.tripadvisor.com/Attraction_Review-g294197-d1958940-Reviews-Hongik_University_Street-Seoul.html"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
browser = webdriver.Chrome("./chromedriver.exe", options=options)

browser.get(URL)

parse(browser.page_source)
