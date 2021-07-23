#!/home/barbara/miniconda/bin/python


"""
Script to automate podecast episode download from Google podcasts
Barbara Abreu
July 2021

This is a script to automate downloads. The downloaded files will be audio files from Fr. Mike's podcast.
I will download them from Google podcasts

"""

import requests
import os
from bs4 import BeautifulSoup


url="https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5maXJlc2lkZS5mbS9iaWJsZWluYXllYXIvcnNz"

response=requests.get(url)

html=response.content

soup=BeautifulSoup(html, 'html.parser')

allr=soup.find_all('c-wiz')[1]

all_links=allr.find_all('div',attrs={'jsaction':"rcuQ6b:vPK81"})

scraped_links=[str(field).split('\"')[5].split(';')[1] for field in all_links]
  
all_descriptions=allr.find_all('div',attrs={'class':"e3ZUqe"})

scraped_desc=list(map(lambda x: x.get_text() , all_descriptions))
adjusted_desc=list(map(lambda x: x.replace(' ','_').replace('\'','-'), scraped_desc))


for i, k in enumerate(zip(scraped_links, adjusted_desc)): 
#    print (i,k)
    str_command='wget '+k[0]+' -O '+str(i)+'_'+k[1]+'.mp3'
    str_wait='sleep 60s'
    print(str_command)
    os.system(str_command)
    os.system(str_wait)




#print (scraped_links)
#print(scraped_desc)
