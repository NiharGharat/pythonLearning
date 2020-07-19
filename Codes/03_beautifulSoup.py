import bs4, requests

#Unable to get data from any of the complex websites

dumpingHtmlFile = "dumpingFolder/htmlDumpingFile.html"
with open(file=dumpingHtmlFile, mode="w") as fp:
    pass


res=requests.get(url="https://automatetheboringstuff.com/2e/chapter12/")
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

exampleFile = open(file=dumpingHtmlFile)
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleFile)

elems = exampleSoup.select('#calibre_link-33 > p:nth-child(139) > span:nth-child(1)')

print(type(elems))
print(len(elems))

print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print("Done")
#TABLE_4