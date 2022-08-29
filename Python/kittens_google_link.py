import requests
from bs4 import BeautifulSoup as beausoup

# User input and verify that it is a real Google link.
kittens_google_link = input("Paste kittens Google link here: https://google.com/ " , verify=True)

# HTTP GET request to get the Google url link.
req = requests.get(kittens_google_link)

# Web scraping the image begins here. 
soup = beausoup(req.content, 'html.parser')

# Use the image tag to find a certain kitten image on Google.
kitten_image = soup.find('img',{'class': 'n3VNCb'})

