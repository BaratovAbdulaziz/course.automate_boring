import requests,bs4
context = requests.get("https://quotes.toscrape.com/")
extracted = bs4.BeautifulSoup(context.text,"html.parser")

result = extracted.find("a")
print(result.text)