import pprint

import requests
from bs4 import BeautifulSoup
import pprint
Url=['https://news.ycombinator.com?p=','https://news.ycombinator.com?p=2']
for i in range(0,2):
    res=requests.get(Url[i]) # get request to page from which we want to scrape data

    print(res) # returns status code
#print(res.text) # displays the entire html file
    soup=BeautifulSoup(res.text,'html.parser') #returns a proper html file
#print(soup.find_all('div')) # returns all div tags in thr html file
#print(soup.a) # returns the first a tag in html file
    links=soup.select('.titlelink') # select enables us grab data with help of css selectors(ID,Classes)
    subtext=soup.select('.subtext')
   # pprint.pprint(links)

def create_custom_hn(links,votes):
    hn=[]
    for inx,item in enumerate(links):
        title=links[inx].getText()
        href=links[inx].get('href',None)
        votes=subtext[inx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            #print(points)
            if points >100:
                hn.append({'title':title,'link':href, 'votes':points})

    return sort_stories_by_votes(hn)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'],reverse=True)

pprint.pprint(create_custom_hn(links,subtext))


