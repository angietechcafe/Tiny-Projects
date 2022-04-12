import requests
from bs4 import BeautifulSoup as beausoup

# user input
kittens_google_link = input("Paste kittens google link here: " )

# HTTP GET request to get the github url link
req = requests.get(kittens_google_link)

# Web scraping the image begins here
soup = beausoup(req.content, 'html.parser')

# Use the image tag to find a certain kitten image on Google.
kitten_image = soup.find('img',{'class': 'n3VNCb'})

