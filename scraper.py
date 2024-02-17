import requests
import os

os_name = os.name

print(os_name)
from bs4 import BeautifulSoup

response = requests.get('https://www.sneakerjagers.com/en/releases')

soup = BeautifulSoup(response.content, 'html.parser')

images = soup.find_all('img')

image_urls = []
for image in images:
    image_url = image['src']
    image_urls.append(image_url)

# Indent the block of code inside the for loop
for image_url in image_urls:
    response = requests.get(image_url)
    with open(os.path.join('images', image_url.split('/')[-1]), 'wb') as f:
        f.write(response.content)