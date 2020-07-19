import os, sys, webbrowser, bs4, requests, pyperclip, re

# 1. Request google with pyperclip args or the once passed with sys.arg
# 2. Dnload the page to the file(Optional)
# 3. Create soup with res.text and html.parser
# 4. find_all on href only with given regex - the regex passed is with href attribute to soup find_all, which is used to apply regex on href attribute
# 5. Get the href complete object with href values
# 6. Apply regex on hrefs to start with https:// and &sa to get actual link
# the search result href -> /url?q=https://docs.python.org/3/tutorial/inputoutput.html&sa=U&ved=2ahUKEwjox4-s4NjqAhXSXSsKHeWeAm4QFjAJegQIAxAB&usg=AOvVaw06pWiQNmtHQ8_VOIvsOoAl
# Search for only href and only get the attribute

def myFunWithOnlyUrl(href):
    return href and re.compile("^/url").search(href)

currentDir = os.getcwd()
argsPassed = ""
if len(sys.argv) > 1:
    print("Args passed were more than 1")
    print(sys.argv)
    argsPassed = " ".join(sys.argv[1:])
else:
    argsPassed = pyperclip.paste()
print("Parsed args were " + argsPassed)

# get the page and download it
googelUrl = "https://www.google.com/search?q="
finalReqParamUrl = googelUrl + argsPassed
print(finalReqParamUrl)
res=requests.get(url=finalReqParamUrl)
res.raise_for_status()

myDumpFolder = currentDir + "/Codes/01_extra/extraDumpingFolder"
if not os.path.exists(myDumpFolder):
    os.makedirs(myDumpFolder)

dumpFileName = myDumpFolder + "/googleSearchFile.html"
print(dumpFileName)
dumpFile = open(file=dumpFileName, mode="a+")
dumpFile.write(res.text)
dumpFile.close()
print("Done writing to file")

soup = bs4.BeautifulSoup(res.content, 'html.parser')
links = soup.find_all(href=myFunWithOnlyUrl)
#links = soup.find_all(name="a", href=myFunWithOnlyUrl)

x = []
for a in links:
    c=re.compile("(https://.*)&sa").search(a['href'])
    print(a['href'])
    #print(c)
    x.append(c.group(1))

for v in x:
    webbrowser.open(v)