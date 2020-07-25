from selenium import webdriver
import re, base64


# This is a program to automatically mail the contents of a file as a string to a destination mail address
# All the necessary credentials will be read from a txt file, proper keys will be assigned the values which will be used later
# in the program
# Strict size and null checks to ensure program fails even if slight mistake in credentials is there
# All email addresses will need to be validated with regex to make sure they are valid
# On opening page need to valided the titles
# Any error in validations, close the browser window first

# Read from given path, and give a dict of credentials
emailAdd = ""
pwd = ""
emailSend = ""
keyNameReadAddress = "readEmailAddress"
keyNameReadPassword = "readEmailPassword"
keyNameSendAddress = "sendEmailAddress"


def closeResource(browser):
    browser.close()


def initCredentials():
    myCredFile = open(file=credFilePath, mode='r')
    cred = {}
    for line in myCredFile:
        key, value = line.strip().split("=")
        cred[key] = value
    myCredFile.close()
    return cred


def initialise_variables():
    global emailAdd, pwd, emailSend
    cred = initCredentials()
    for key in cred.keys():
        print(key)
        print(cred[key])
        if key == keyNameReadAddress:
            emailAdd = cred[key]
        elif key == keyNameReadPassword:
            pwd = cred[key]
        else:
            emailSend = cred[key]


# S1: read from cred file and get the credentials in a map
credFilePath = "/home/nihar/Desktop/credFile.txt"
initialise_variables()
print("All variables inited")


# S2: Start the session on browser and validate page name
_GOOGLE_URL = "https://mail.google.com/mail/u/2/#inbox"
_validationLoginPageTitle = 'Gmail'
browser = webdriver.Firefox()
browser.get(_GOOGLE_URL)
print(browser.title)
if browser.title != _validationLoginPageTitle:
    closeResource(browser)
    raise Exception("Incorrect page opened")
print("Session opened in browser")


# S3: Login with credentials and validate page name on regex
loginEmailSelector = "html.CMgTXc body#yDmH0d.nyoS7c.SoDlKd.EIlDfe div.H2SoFe.LZgQXe.TFhTPc div#initialView.RAYh1e.LZgQXe.qmmlRd div.xkfVF div.Aa1VU div#view_container.JhUD8d.SQNfcc.vLGJgb div.zWl5kd div.DRS7Fe.bxPAYd.k6Zj8d div.pwWryf.bxPAYd div.Wxwduf.Us7fWe.JhUD8d div.WEQkZc div.bCAAsb form span section.aTzEhb div.CxRgyd div div.d2CFce.cDSmF div.rFrNMe.N3Hzgf.jjwyfe.vHVGub.zKHdkd.sdJrJc.Tyc9J div.aCsJod.oJeWuf div.aXBtI.Wic03c div.Xb9hP input#identifierId.whsOnd.zHQkBf"
nextButton = "html.CMgTXc body#yDmH0d.nyoS7c.SoDlKd.EIlDfe div.H2SoFe.LZgQXe.TFhTPc div#initialView.RAYh1e.LZgQXe.qmmlRd div.xkfVF div.Aa1VU div#view_container.JhUD8d.SQNfcc.vLGJgb div.zWl5kd div.DRS7Fe.bxPAYd.k6Zj8d div.pwWryf.bxPAYd div.Wxwduf.Us7fWe.JhUD8d div.zQJV3 div.dG5hZc div.qhFLie div#identifierNext.FliLIb.DL0QTb div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc"
passwordSelector = ".I0VJ4d > div:nth-child(1) > input:nth-child(1)"
loginButton = "html.CMgTXc body#yDmH0d.nyoS7c.SoDlKd.EIlDfe div.H2SoFe.LZgQXe.TFhTPc div#initialView.RAYh1e.LZgQXe.qmmlRd div.xkfVF div.Aa1VU div#view_container.JhUD8d.SQNfcc.vLGJgb div.zWl5kd div.DRS7Fe.bxPAYd.k6Zj8d div.pwWryf.bxPAYd div.Wxwduf.Us7fWe.JhUD8d div.zQJV3 div.dG5hZc div.qhFLie div#passwordNext.FliLIb.DL0QTb div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc"

try:
    loginEmail = browser.find_element_by_css_selector(loginEmailSelector)
    loginEmail.clear()
    loginEmail.send_keys(emailAdd)
    buttomNext=browser.find_element_by_css_selector(nextButton)
    buttomNext.click()
    passwordField=browser.find_element_by_css_selector(passwordSelector)
    passwordField.clear()
    passwordField.send_keys(pwd)
    loginButton=browser.find_element_by_css_selector(loginButton)
    loginButton.click()
    input("Solve the login validation and enter any key to continue")
    print(browser.title)
    if not browser.title.startswith("Inbox "):
        closeResource(browser)
        raise Exception("Incorrect page opened")
except Exception as e:
    print(e)
    closeResource(browser)
    print("Error in step three, logging in")
    raise Exception("Error in step three, logging in")
print("Loggin successful")


# S4: Create text to send to the body
bodyContent=[]
f2=open("/home/nihar/Desktop/FileWithDataToPush.txt", 'r')
for f in f2:
    bodyContent.append(f)
f2.close()
print("File read, and data stored, length of data is " + str(len(bodyContent)))


# S5: Compose email and send
composeEmailButton = ".T-I-KE"
subjectLineSelector = "aoT"
toEmailSelector = "#\:8x"
bodySelector = "#\:9k"
sendButton = "#\:85"
try:
    composeEmail=browser.find_element_by_css_selector(composeEmailButton)
    toEmail=browser.find_element_by_css_selector(toEmailSelector)
    toEmail.clear()
    toEmail.send_keys(emailSend)
    subjectLine=browser.find_element_by_class_name(subjectLineSelector)
    subjectIp = input("Enter the subject line for the email")
    subjectLine.send_keys(subjectLine)
    bodyElem=browser.find_element_by_css_selector(bodySelector)
    bodyElem.clear()
    bodyElem.send_keys(f)
    sendButton=browser.find_element_by_css_selector(sendButton)
    sendButton.click()
except Exception as e:
    print(e)
    closeResource(browser)
    print("Error in step five, Entering content in subject and body lines")
    raise Exception("Error in step five, Entering content in subject and body lines")


# S6: logout
logoutButton = "html.aAX body.aAU div div.nH div.nH div.nH.w-asV.aiw div.nH.oy8Mbf.qp header#gb.gb_sa.gb_4a.gb_9e.gb_Oc div.gb_3d.gb_le.gb_ce div.gb_3c.gb_0a.gb_2c.gb_ie div.gb_4c div.gb_Ua.gb_nd.gb_Pg.gb_i.gb_1f div.gb_0f.gb_Za.gb_Pg.gb_i a.gb_D.gb_Ta.gb_i"
actualLogOut = "gb_71"
try:
    logoutButton=browser.find_element_by_css_selector(logoutButton)
    logoutButton.click()
    logoutButtonActual=browser.find_element_by_id(actualLogOut)
    logoutButtonActual.click()
except Exception as e:
    print(e)
    closeResource(browser)
    print("Error occured while logging out")
    raise Exception("Error occured while logging out")

print("All done, closing")
browser.quit()
print("Done")
