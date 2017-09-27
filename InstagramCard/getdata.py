from bs4 import BeautifulSoup
import requests
import lxml
import urllib
from urllib.request import urlopen
import re
import json
import math
from math import floor
from json import load

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def userprofile(username):
    url = 'http://instagram.com/'+str(username)+'/?__a=1'
    response=urlopen(url)
    jsonobj=load(response)
    detail=jsonobj["user"]["biography"]
    followers=jsonobj["user"]["followed_by"]["count"]
    if 1000000>int(followers)>=1000:
        followers=str(truncate(float(followers/1000),1))+'k'
    elif int(followers)>=1000000:
        followers=str(truncate(float(followers/1000000),1))+'m'
    
    following=jsonobj["user"]["follows"]["count"]
    if 1000000>int(following)>=1000:
        following=str(truncate(float(following/1000),1))+'k'
    elif int(following)>=1000000:
        following=str(truncate(float(following/1000000),1))+'m'
    image_link=jsonobj["user"]["profile_pic_url"]
    name=jsonobj["user"]["full_name"]
    posts=jsonobj["user"]["media"]["count"]
    link=jsonobj["user"]["external_url"]
    
    return(url,image_link,link,name,detail,posts,followers,following)
