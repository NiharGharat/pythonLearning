import requests

urlOfFile = "https://automatetheboringstuff.com/files/rj.txt"
fileName = "dumpingFolder/myFileToWriteTo.txt"
res = requests.get(url=urlOfFile)

print(res.status_code)
try:
    res.raise_for_status()
    # dump it to file
    dumpFile = open(file=fileName, mode="wb")

    for chunk in res.iter_content(100000):
        dumpFile.write(chunk)

    dumpFile.close()
except Exception as exc:
    print("There was a problem downloading the file from your specified url")
    print("Stack was %s" % (exc))

print("...Exit...")