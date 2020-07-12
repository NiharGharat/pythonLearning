import webbrowser, sys

print(sys.argv)
address = ""
if (len(sys.argv)) > 1:
    address = " ".join(sys.argv[1:])

print("Join address created was " + address)

maps_ = "https://www.google.com/maps/place/"
finalAddress = "Website to push to is maps " + maps_ + address
print("Final web address is " + finalAddress)

webbrowser.open(maps_ + address)