import time

import requests
from requests import get

from bs4 import BeautifulSoup

domain = "https://w13.mangafreak.net"

page = requests.get("https://w13.mangafreak.net/Manga/Onepunch_Man", verify=False, timeout=5)

html = page.text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('a'):
    url = link.get('href')
    if "images" in url:
        print(url)
        file_name = url.split("downloads/", 1)[1]
        with open(file_name +'.zip',"wb") as files:
            response = get(url)
            print(response)
            files.write(response.content)
    else:
        continue






