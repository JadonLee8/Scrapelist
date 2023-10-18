from bs4 import BeautifulSoup
import requests

search_query = input("Enter search query: ")

r = requests.get('https://austin.craigslist.org/search/sss?query=' + search_query + '#search=1~list~0~0')

# check status code for response received 
# success code - 200 
print(r) 

# get content with r.content()

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
# print(soup.prettify()) 

