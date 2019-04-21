import re
import requests
from bs4 import BeautifulSoup


session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'


headers = {}

headers['User-agent'] = "HotJava/1.1.2 FCS"
response = session.get('https://www.httpbin.org', headers=headers)


soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


links = []
for link in soup.findAll('a'):
    pic_link = link.get('href')
    if pic_link is not None:
        if 'jpg'in pic_link:
            links.append(pic_link)

print('size of links is : ')
print(len(links))

for url in links:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if filename is not None:
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                # sometimes an image source can be relative
                # if it is provide the base url which also happens
                # to be the site variable atm.
                url = '{}{}'.format(site, url)
            response = session.get(url)
            f.write(response.content)
