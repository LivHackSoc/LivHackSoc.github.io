# Deploy bot for Python
# TODO
# check all links on page for 404
# check all images to see if they have an alt text
# compress html
# compress javascript
# compress css

import requests
import re, queue, threading
import check_link
from bs4 import BeautifulSoup
import urllib.request

def get_all_links(address):
    resp = urllib.request.urlopen("http://www.gpsbasecamp.com/national-parks")
    soup = BeautifulSoup(urllib.request.urlopen("http://www.gpsbasecamp.com/national-parks"), from_encoding=resp.info().get_param('charset'))
    return [link['href'] for link in soup.find_all('a', href=True)]

def threader():
    while True:
        value = q.get()  
        result = extract_link(value)
        q.task_done()

if __name__=="__main__":
    colorama.init()
    q = queue.Queue()
    global hyperlinks, website
    hyperlinks = set()
    website = input("Please enter the website address: ") 
    for x in range(30):
        t = threading.Thread(target=threader)
        t.deamon=True
        t.start()   
    q.put(website.strip())
    q.join()