from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re

def fun1():
    html = urlopen("http://192.168.40.130:8089/index/")
    bsObj = BeautifulSoup(html.read())
    print(bsObj.h1)
    print(bsObj.html.body.h1)

# fun1()

def fun2_getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:      
        print("Title could not be found")
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        # title = bsObj.html.body.h1
        title = bsObj        
        print(title)
    except AttributeError as e:
        return None
    # return title

# title1 = "http://192.168.40.130:8089/index.html"
title1 = "http://192.168.40.130:8089/index"
# fun2_getTitle(title1)

# if title == None:
#     print("Title could not be found")
# else:
#     print(title)

def fun3():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)

    for child in bsObj.find("table", {"id":"giftList"}).children:
        print(child)
    for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_sibling:
        print(sibling)

# fun3()

def fun4():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    # html = urlopen("http://www.baidu.com")    
    bsObj = BeautifulSoup(html, "html.parser")
    images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    for images in images:
        print(images["src"])
    
# fun4()

def fun5():
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])
# fun5()

def fun6():
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                        href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])

fun6()








