import webbrowser, re, bs4, pyperclip, requests

# This module is only

# Google search url to append args to
GOOGLE_URL_ = "https://www.google.com/search?q="
# Google gives urls as /url?q=https://www.w3schools.com/python/python_file_write.asp&sa=U&ved=2ahUKEwjvsYH18NjqAhWnxDgGHa7pCusQFjAAegQIAhAB&usg=AOvVaw0cUsg4wlTlaHQbu4PyQRY0
# Hence regex to give ONLY the href
def myRegexForGoogleSearchUrl(href):
    return href and re.compile("^/url").search(href)

# Construct the args url
argsPassed = pyperclip.paste()
if len(argsPassed) == 0:
    raise Exception("Pyperclip only supported; ensure agrs are in clipboard")
finalReqParamUrl = GOOGLE_URL_ + argsPassed

print("Final url to pass to search is " + argsPassed)

res=requests.get(url=finalReqParamUrl)
res.raise_for_status()

# Pass the request string to bs4 to create soup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Use observed and created regex to get links of all the search results
links = soup.find_all(href=myRegexForGoogleSearchUrl)

# Within each /url link as well, need to extract https:// part and till &sa
regexExtractPattern = "(https://.*)&sa"
x = []
for link in links:
    c = re.compile(regexExtractPattern).search(link['href'])
    x.append(c.group(1))

# At this point we have all the links from page 1
# Debug
for a in x:
    print(a)

# Open 1st to check
webbrowser.open(x[0])

# Done