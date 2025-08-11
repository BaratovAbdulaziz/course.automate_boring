import bs4
with open("/home/abdulaziz/workspace/course.automate_boring/Notebooks/Chapter-12/bs4_testing.html","r") as source:
    extracted = bs4.BeautifulSoup(source,"html.parser")
    print(extracted.text)
