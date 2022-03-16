import requests
from bs4 import BeautifulSoup

# user input
Github_link = input("Paste Github user link here: " )
# -> angieintech
# HTTP get request to get the github url link
r = requests.get(Github_link)

