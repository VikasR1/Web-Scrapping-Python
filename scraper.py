import requests
import urllib.request
from bs4 import BeautifulSoup
import os

url = 'https://www.bridgeport.edu/'

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}
# make a request to url
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# download all the images 
image = soup.find_all('img')

i = 0
for im in image:
    i = i+1
    # taking image path from src tag
    image_temp = im.get('src')
    if image_temp[:1] == '/':
        image_path = "https://www.bridgeport.edu" + image_temp
    else:
        image_path = image_temp

#  dlwnloading images with their extentions
    if '.jpg' in image_path:

        with open("{}.jpg".format(i), 'wb') as f:
            f.write(requests.get(image_path).content)
    else:
        pass
    

      


