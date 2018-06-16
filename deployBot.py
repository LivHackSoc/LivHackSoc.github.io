# Deploy bot for Python
# TODO
# [X] check all links on page for 404
# check all images to see if they have an alt text
# compress html
# compress javascript
# compress css

import check_link
from bs4 import BeautifulSoup
import urllib.request
from multiprocessing import Process

# creates a global check_link object
check_link_obj = check_link.check_link()

def get_all_links(address):
    # get all links on a website, return a set
    resp = urllib.request.urlopen(address)
    soup = BeautifulSoup(resp, 'html.parser')
    links = soup.find_all('a')
    return set([link.get('href') for link in links
                if link.get('href') and link.get('href')[0:4]=='http'])

def threader(website):
    # this function is used to create new threads
    response = check_link_obj.check(website)
    if response != True:
        print("HTTP " + str(response) + " " +  website)

def main():
    # creates new threads of threader, starts them then joins them together
    website = input("What is the address of the website? ")
    all_links = get_all_links(website)
    for i in all_links:
        try:
            Process(target = threader, args = (i, )).start()
        except Exception as e:
            pass

if __name__=="__main__":
    main()
