# pythonLearning

The main aim to to be capable enough for scrapping a <specific> site, and download a particular data from it.
  
This is just the learning path for the same.

# S1
- Made a python executable with bash script in a directory and NOT gave a hardcoded path to the file.
- 01_openMapAddress.py
  - Modules used	-> pyperclip, sys, webbrowser
  - Pyperclip			-> copy from clipboard
	- sys						-> make program capable to read from passed system args
	- webbrowser		-> open the web browser
  - Push to google maps address.
	- Algo.
		- Construct the correct url with given args, they are joined on string to get correct request param to pass to google maps
		- pass them to web browser module
