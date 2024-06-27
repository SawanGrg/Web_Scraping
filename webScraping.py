import requests as req
import pandas as pd
from bs4 import BeautifulSoup

root_url = 'https://quotes.toscrape.com/page/'
page_initial_size = 1

file_path = 'D:\holder.txt'

def extract_quotes(divs):
    quotes = []
    for tag in divs:
        quote = tag.find('span', attrs={'class': 'text'})
        quotes.append(quote.text.strip())
    return quotes

def extract_authors(divs):
    authors = []
    for tag in divs:
        author = tag.find('small', attrs={'class': 'author'})
        authors.append(author.text.strip())
    return authors


def extract_tags(divs):
    tags = []
    for div in divs:
        tag_elements = div.find_all('div', class_='tags')
        for tag in tag_elements:
            each_tag = tag.find('a', class_='tag')
            tags.append(each_tag.text)
    return tags

with open(file_path, "a+", encoding="utf-8") as f:

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
            authors = extract_authors(quote_divs)
            tags = extract_tags(quote_divs)

            for q, a, t in zip(quotes, authors, tags):
                    formatted_quote = f'"{q}" - {a} [{t}]'
                    print(formatted_quote)
                    f.write(formatted_quote + "\n")
