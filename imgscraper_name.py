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
print(r)
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

    # taking image name from alt tag
    image_name_temp = im.get('alt')

    if len(image_name_temp) == 0:
        image_name = str(i)
    else:
        image_name = image_name_temp

#  getting images with jpg extentions
    if '.jpg' in image_path:
        c_wd = os.getcwd()

        try:
            os.makedirs('IMAGES/JPEG')
        except:
            folder_dir = c_wd + '/IMAGES/JPEG'
            name_file = "{}.jpg".format(image_name)

            final_path = os.path.join(folder_dir, name_file )

            with open(final_path, 'wb') as f:
                f.write(requests.get(image_path).content)
                print('writing: ', name_file)
    else:
        pass

#  getting images with png extentions
    if '.png' in image_path:
        c_wd = os.getcwd()

        try:
            os.makedirs('IMAGES/PNG')
        except:
            folder_dir = c_wd + '/IMAGES/PNG'
            name_file = "{}.png".format(image_name)

            final_path = os.path.join(folder_dir, name_file )

            with open(final_path, 'wb') as f:
                f.write(requests.get(image_path).content)
                print('writing: ', name_file)
    else:
        pass
    

      


