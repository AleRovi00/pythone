import urllib.request
url = "https://www.acmilan.com/it"
risultato = urllib.request.urlopen(url)
theBytes = risultato.read()
text = theBytes.decode()
import bs4
doc = bs4.BeautifulSoup(text)
print(doc.prettify())


def naviga3(tag) :
    if tag.name.upper() == "A":
        print (tag.get("href"))
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga3(stag)

naviga3(doc)