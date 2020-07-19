import requests, bs4, os, re

currentDir = os.getcwd()
URL_ = "https://html.com/"
DOWNLOAD_FOLDER_ = currentDir + "/dumpingFolder/"
if not os.path.exists(DOWNLOAD_FOLDER_):
    os.makedirs(DOWNLOAD_FOLDER_)
    print("Folder created for write")

res = requests.get(url=URL_)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
allHrefsLinks = soup.find_all(href=re.compile("^https://.*/"))

for i in allHrefsLinks:
    print(i['href'])

# traverse first 5 links and dnload the page

count = 0;
for i in allHrefsLinks:
    resX = requests.get(i['href'])
    dumpFileName = DOWNLOAD_FOLDER_ + "file" + str(count) + ".html"
    count += 1
    dumpFile = open(dumpFileName, 'wb')
    for chunk in resX.iter_content(100000):
        dumpFile.write(chunk)
    dumpFile.close()
    print("Write done for file " + str(count))
    if count > 5:
        break

print("All done, files written are " + str(count))