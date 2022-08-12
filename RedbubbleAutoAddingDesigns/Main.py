# Setup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import os
import glob

PATH = "C:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.redbubble.com/")

# Info
username = ""
password = ""
print(driver.title)

# picture from directory
file_path = './pictures/'
picture = ""
print(file_path)


title = "Artificial Intelligence"
tags = "love, dinosaur, dino, monster, cat, dog, swag, fantastic, kraken, dragon, parrot, family, art, Artificial Intelligence, cyborg, life"
description = "This picture is made by an Artificial Intelligence, and are describing random things the Artificial Intelligence thinks about. No images ever made from this Artificial Intelligence are and will be the same!"


time.sleep(15)
try:
    # Tar bort cookie knappen
    search = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    time.sleep(5)
except NoSuchAttributeException:
    print("Cant find cookie button to allow it")
except:
    print("No fucking cookie button")


    # Går till inloggnings fönstret
search = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div/div/header/div[1]/a[2]').click()
time.sleep(15)


time.sleep(10)
#Inputing username and password

time.sleep(5)
driver.refresh()
print("Refreshing!")
# Loggar in
search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[1]/div/div/input')
search.send_keys(username)
search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[2]/div/div/input')
search.send_keys(password)

search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/span/button').click()

try:
    # Tar bort start cookisen
    search = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
    time.sleep(5)
except NoSuchAttributeException:
    print("Cant find cookie button to allow it")
except:
    print("No fucking cookie button")
time.sleep(60)
driver.refresh()
print("Refreshing!")
time.sleep(25)
driver.refresh()
print("Refreshing!")
time.sleep(15)
driver.refresh()
print("Refreshing!")

try:
    # Random popup
    if driver.find_element_by_xpath('/html/body/div[1]/div[7]/button'):
        driver.refresh()

except:
    print("No fucking random popup!")

play = True
number = 0

while(play == True):
    time.sleep(5)
    # Första bilden i mappen lägs in i picture
    try:
        picture = os.listdir(file_path)[number]
        print(picture)
        print(type(picture))
    except NoSuchAttributeException:
        print("Cant find any picture")
    except:
        print("Picture problem")

    try:
        # Tar bort start cookisen
        search = driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
        time.sleep(5)
    except NoSuchAttributeException:
        print("Cant find cookie button to allow it")
    except:
        print("No fucking cookie button")


    time.sleep(5)
    # Letar efter profil bilden
    search = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/div/header/div[3]/div[1]/div/div/div/div[1]/div/div/div/button').click()

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    time.sleep(5)
    # klickar på add new work
    search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/header/div[3]/div[1]/div/div/div/div[2]/div/div/div/div/div/ul[1]/div[1]/a').click()

    driver.refresh()
    print("Refreshing!")

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")


    time.sleep(5)
    # behöver lägga till något system som läser upp från en map och sedan tar första i mapen och lägger in, efter den är klar med att spara allt till sidan så tar den bort den bilden från mapen.
    # Lägger till en bild
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[1]/div[1]/input').send_keys(os.getcwd() + file_path +picture)

    if os.path.isfile(file_path + picture) == True:
        os.remove(picture)
    else:
        picture = os.listdir(file_path)[number] + 1

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # Title
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[1]/input').send_keys(title)
    print("Adding Title")

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # Tags
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[2]/textarea').send_keys(tags)
    print("Adding Tags")

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # Description
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[3]/textarea').send_keys(description)
    print("Adding Description")

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # Is this mature content?
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[2]/div[2]/div/label[2]/input').click()

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # I have read this and accept that its my design
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[3]/input').click()


    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # Save button
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[4]/div/input').click()

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    time.sleep(25)

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")

    # Go back to start page
    time.sleep(5)
    search = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div/div/header/div[2]/a/svg').click()

    try:
        # Random popup
        search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/button').click()
    except:
        print("No fucking random popup!")



