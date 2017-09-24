from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import lxml
import urllib
import time
from urllib.request import urlopen
from pyvirtualdisplay import Display
import re


def userprofile(username):
    url = 'http://instagram.com/'+str(username)+'/'
    
    
    display = Display(visible=0, size=(800, 600))
    display.start()

    chromedriver_loc = '/app/chromedriver-Linux64' # enter path of chromedriver
    driver = webdriver.Chrome(executable_path=chromedriver_loc)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,"lxml")
    image_link = soup.find('img', {'class':'_9bt3u'})['src']
    u = soup.find('article',{'class':'_mesn5'})
    text = (u.text)
    link = None
    description = soup.find('div',{'class':'_tb97a'})
    name = description.find('h2',{'class':'_kc4z2'}).text
    detail = description.text.split(name,1)[1]
    i=description.find('a',{'class':'_ng0lj'})
    if i :
        link=i.text
        detail=detail.split(link,1)[0]

    m = re.search('Follow(.+?) ', text)
    posts=m.group(1)

    m = re.search('posts(.+?) ', text)
    followers=m.group(1)

    m = re.search('followers(.+?) ', text)
    following=m.group(1)
    driver.quit()
    display.stop()
    
    return(url,image_link,link,name,detail,posts,followers,following)
