import requests, bs4, os

XKCD_URL_ = "https://xkcd.com/"

res = requests.get(url=XKCD_URL_)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
img = soup.select("#comic > img")

comicUrl = "https:" + img[0].get("src")
print(comicUrl)
res = requests.get(comicUrl)
res.raise_for_status()

currentDir = os.getcwd()
if not os.path.exists(currentDir + "/dumpFolder/"):
    os.makedirs(currentDir + "/dumpFolder/")

imageFile = open(currentDir + "/dumpFolder/" + os.path.basename(comicUrl), 'wb')
for chunk in res.iter_content(10000):
    imageFile.write(chunk)

imageFile.close()

# Highlights
# 1. Using css selector to get specific tag, also getting the name of the file using os module
# 2. Downloading an image file, using chunk writer to write the image in current directory