import requests
from bs4 import BeautifulSoup
#import MyFunction

url = "https://www.procyclingstats.com/rider/tadej-pogacar"
req = requests.get(url)
page = BeautifulSoup(req.text, "html.parser")

# rdr-info-cont

info = page.find(class_="rdr-info-cont")

info_split1 = info.text.split("\n")

print(info_split1)


