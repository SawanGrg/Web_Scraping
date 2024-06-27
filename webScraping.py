import requests as req
import pandas as pd
from bs4 import BeautifulSoup

root_url = 'https://quotes.toscrape.com/page/'
page_initial_size = 1

#pachi we can break down this code into SOLID Acronym ko first principle: Single Responsibility Principle
def extract_quotes(divs):
        quotes = []
        for tag in divs:
            quote = tag.find('span', attrs = {'class':'text'})
            quotes.append(quote.text)

            f = open("D:\holder.txt", "a+", encoding="utf-8")
            f.write(quote.text + "\n")
        return quotes

#pachi we break down this code into SOLID Acronym ko first principle: single responsibility principle
def extract_author(divs):
        authors = []
        for tag in divs:
            author = tag.find('small', attrs = {'class':'author'})
            authors.append(author.text)
            f = open("D:\holder.txt", "a+", encoding="utf-8")
            f.write(author.text + "\n")
        return authors


#time complexity: O(n) huncha hai dai esko 
#for each iteration, we are making a request to the server and parsing the response with new pagination
for i in range(1, 4):
    response = req.get(root_url + str(i))

    if response.status_code == 200:
        print("Request was successful")
    else:
        print("Request failed")

    soup = BeautifulSoup(response.text, 'html.parser')

    quote_divs = soup.find_all('div', attrs={'class': 'quote'})

    quotes = extract_quotes(quote_divs)
    authors = extract_author(quote_divs)

    for quote in quotes:
        print(quote)

    for author in authors:
        print(author)
