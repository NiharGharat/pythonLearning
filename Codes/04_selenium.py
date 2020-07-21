from selenium import webdriver
import webbrowser, os, pyperclip, bs4

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

elem = browser.find_element_by_css_selector("body > div.container > div:nth-child(3) > div > center > a:nth-child(1) > img")
elem.click()


