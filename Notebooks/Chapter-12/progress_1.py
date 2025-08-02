import requests
context = requests.get("https://example.com")
print(context.text)
from bs4 import BeautifulSoup
extract = BeautifulSoup(context.text, "html.parser")
title = extract.find("title")
print(title.text)