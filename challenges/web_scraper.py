## www.dailysmarty.com/topics/python Scraper ##

'''
parse through all the html data and we scrape all the a links that go to posts/articles
build a function to convert html link to page title with .title()

Example of Final Output:
"How to Implement FizzBuzz in Python"
"Installing Anaconda Python Data Science Platform"
"Python SCript for Pulling in the Same Column from an Array of Arrays"

Recommended to use libraries:
  -Requests
  -Inflection
  -beautifulsoup4
  
can use traditional pip for most of these
'''

import requests # adds request functionality
import inflection # inflection.humanize(word) can be used to fix strings 
import pprint # makes pretty
from bs4 import BeautifulSoup # adds web scraping functionality

def web_scraper(link):
    website = requests.get(link)
    soup = BeautifulSoup(website.content, 'html.parser')
    print(soup) # titles include data-turbolinks - a links
    links = soup.find_all('a')

    for link in links:
      print(link['href'])

web_scraper('http://www.dailysmarty.com/topics/python')