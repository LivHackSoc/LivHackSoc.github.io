# Deploy bot for Python
# TODO
# check all links on page for 404
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
    # get all links on a website, return a list
    resp = urllib.request.urlopen("http://www.gpsbasecamp.com/national-parks")
    soup = BeautifulSoup(urllib.request.urlopen("http://www.gpsbasecamp.com/national-parks"), from_encoding=resp.info().get_param('charset'))
    return set([link['href'] for link in soup.find_all('a', href=True)])

def threader(website):
    # this function is used to create new threads
    check_link_obj.check(website)

def main():
    # creates new threads of threader, starts them then joins them together
    website = input("What is the address of the website? ")
    all_links = get_all_links(website)
    processes = [Process(target = threader, args = (i)) for i in all_links]
    map(lambda x: x.start(), processes)
    map(lambda y: y.join(), processes)

if __name__=="__main__":
    main()
