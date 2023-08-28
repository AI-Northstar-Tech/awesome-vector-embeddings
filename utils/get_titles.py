import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else url[:20]
        return title
    else:
        return 'Failed to Retrieve'

url = 'https://www.google.com'
title = fetch_title(url)
markdown_link = f'[{title}]({url})'
print(markdown_link)
