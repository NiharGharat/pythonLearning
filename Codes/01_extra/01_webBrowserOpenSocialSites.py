import webbrowser

sites = []
file = open(file="theSitesToOpen.txt", mode='r')
for line in file:
    sites.append(line)

for site in sites:
    print("Sites to open " + site)
    webbrowser.open(url=site)

file.close()
print("...Exit...")