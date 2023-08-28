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
new_file = ''
# read file ../README.md
with open('../README.md', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('1. '):
            # parse url
            if '](' in line:
                url = line.split('](')[1].split(')')[0]
            else:
                url = line.split('1. ')[1].strip()
            # fetch title
            title = fetch_title(url)
            # replace title
            new_line = f'1. [{title} {url}: ]({url})\n'
            # print(new_line)
            print(new_line, end='')
        else:
            new_line = line
            print(line, end='')
        new_file += new_line
# write file ../README.md
with open('../README.md', 'w') as f:
    f.write(new_file)
# print(fetch_title('https://www.google.com'))

        
# url = 'https://www.google.com'
# title = fetch_title(url)
# markdown_link = f'[{title}]({url})'
# print(markdown_link)
