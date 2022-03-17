import requests
from bs4 import BeautifulSoup as beausoup

# user input
Github_link = input("Paste Github user link here: " )
# -> angieintech
# HTTP GET request to get the github url link
req = requests.get(Github_link)
# Web scraping the image begins here
soup = beausoup(req.content, 'html.parser')
# Use the image tag to find a certain image on Github.
# certain_image = soup.find('img',{'some tag here': 'tag description here'})

