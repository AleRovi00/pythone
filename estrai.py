import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")

import bs4
doc = bs4.BeautifulSoup(text)
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag :
        tds = tr.contents
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".",""))
        sigl = tds[7].get_text()
        sup = int(tds[4].get_text().replace(".",""))
        dens= tds[5].get_text().replace(".","").replace(",",".")
        densf= float(dens)
        calcolo = round(resi / sup, 1)
        if calcolo == densf:
            print(f"{sigl} {prov:25s} {resi:9d} {sup:5d} {densf:6.1f} {calcolo:6.1f} OK")
        else:
            print(f"{sigl} {prov:25s} {resi:9d} {sup:5d} {densf:6.1f} {calcolo:6.1f} ERR")
        #print(f"{sigl} {prov:25s} {resi:9d} {sup:5d} {densf:6.1f} {calcolo:6.1f} ")