#Author Filip Malmberg

import os
import sys
import ctypes
import time
import subprocess
import platform
import random
import getpass

from pick import pick
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

emoji = u'\U0001F44D' #Thumbs up emoji

email = input("Enter your email: ")
password = getpass.getpass()

title = 'What would you like to do?: '
options = ['Like/comment company feed', 'Like/comment group feed', 'Post to group feed']
option, index = pick(options, title)
print(option)
print(index)

if index == 0:
    print('Updating company feed!')
elif index == 1:
    print('Updating group feed!')
elif index == 2:
    print('Posting something motivational to group feed!')

driver = webdriver.Firefox()
driver.get('https://weplusapp.com')
driver.implicitly_wait(20)
logincheck = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/form/div[3]/a[1]"))).text
if logincheck:
    emailfield = driver.find_element(by=By.ID, value="email")
    passwordfield = driver.find_element(by=By.ID, value="password")
    emailfield.send_keys(email)
    time.sleep(1)
    passwordfield.send_keys(password)
    loginbutton = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/form/div[3]/input").click()
driver.implicitly_wait(20)
time.sleep(1)

if index == 0:
    companybutton = driver.find_element(by=By.XPATH, value="/html/body/ul[1]/li[2]/a")
    companybutton.click()
    driver.implicitly_wait(20)
    time.sleep(1)
    select = Select(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/div/form/div[1]/div[1]/div/select"))
    select.select_by_value("created-at")
    driver.implicitly_wait(20)
    time.sleep(1)
    selectall = Select(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/div/form/div[1]/div[2]/div/select"))
    selectall.select_by_value("all")
    driver.implicitly_wait(20)
    time.sleep(1)

elif index == 1:
    groupbutton = driver.find_element(by=By.XPATH, value="/html/body/ul[1]/li[1]/a")
    groupbutton.click()
    driver.implicitly_wait(20)
    time.sleep(1)
    select = Select(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/div[2]/form/div[1]/div[1]/div/select"))
    select.select_by_value("created-at")
    driver.implicitly_wait(20)
    time.sleep(1)
    selectall = Select(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/div[2]/form/div[1]/div[2]/div/select"))
    selectall.select_by_value("all")
    driver.implicitly_wait(20)
    time.sleep(1)

elif index == 2:
    groupbutton = driver.find_element(by=By.XPATH, value="/html/body/ul[1]/li[1]/a")
    groupbutton.click()
    driver.implicitly_wait(20)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/div[1]/div/div/ul/li[2]/a").click() #Click on post button
    driver.implicitly_wait(20)
    time.sleep(1)
    driver.find_element

i = 1
while True:
    print(i)
    if i == 7 or i == 13 or i == 19 or i == 25 or i == 31 or i == 37 or i == 43 or i == 49 or i == 55 or i == 61:
        if index == 0:
            morebutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/ul/li[{}]/a".format(i)).click()
            driver.implicitly_wait(20)
        elif index == 1:
            morebutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/ul/li[{}]/a".format(i)).click()
            driver.implicitly_wait(20)
    time.sleep(1)
    if index == 0: #Company feed
        postpath = "/html/body/div[2]/div[4]/div/ul/li[{}]".format(i)
        post = driver.find_element(by=By.XPATH, value=postpath).click()
        driver.implicitly_wait(20)
        time.sleep(1)
        namefield = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/ul/li/div/div[1]/div/h3/strong"))).text
        name = namefield.split(' ')[0] #Select firstname
        try:
            likebutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/ul/li/div/ul/li/a") #Look for a like button
        except Exception:
            print("Likebutton not found!")
            input("Script finished. Press any button to exit.")
            driver.close()
            break
        print("Clicking likebutton on {}'s post".format(name))
        likebutton.click()
        time.sleep(1)
        commentlist = [
                        "Good job {}! {}{}".format(name,emoji,emoji),
                        "Keep up the good work {}! {}{}".format(name,emoji,emoji),
                        "Awesome! Keep it up {}! {}{}".format(name,emoji,emoji),
                        "Nice one {}! You inspire us all! {}{}".format(name,emoji,emoji),
                        "Keep it up {}! {}{}".format(name,emoji,emoji),
                        "Nice one {}! {}{}".format(name,emoji,emoji),
                        "Rock on {}! {}{}".format(name,emoji,emoji),
                        "You're an inspiration to us all, {}! {}{}".format(name,emoji,emoji),
                        "Wow! Such dedication {}! {}{}".format(name,emoji,emoji),
                        "Way to go {}! {}{}".format(name,emoji,emoji),
                        "I wish I had your energy, {}! {}{}".format(name,emoji,emoji),
                        "Keep it going {}, we'll get there together! {}{}".format(name,emoji,emoji),
                        "No brakes on this {}-train! {}{}".format(name,emoji,emoji),
                        "All aboard the {}-fitnesstrain! Choo choo! {}{}".format(name,emoji,emoji)
                        ]
        comment = random.choice(commentlist)
        print("Commenting on {}'s post".format(name))
        commentfield = driver.find_element(by=By.XPATH, value="""//*[@id="comment_body"]""")
        commentfield.send_keys(comment)
        print(comment)
        time.sleep(1)
        commentfield.send_keys(Keys.RETURN)
        time.sleep(1)
        xbutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/a").click()
        time.sleep(1)

    elif index == 1: #Group feed
        try:
            likebutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div/ul/li/a".format(i)) #Look for a like button
        except Exception:
            print("Likebutton not found!")
            input("Script finished. Press any button to exit.")
            driver.close()
            break
        print("Clicking likebutton")
        likebutton.click()
        time.sleep(1)
        commentlist = [
                        "Good job! {}{}".format(emoji,emoji),
                        "Keep up the good work! {}{}".format(emoji,emoji),
                        "Awesome! Keep it up! {}{}".format(emoji,emoji),
                        "Nice one! You inspire us all! {}{}".format(emoji,emoji),
                        "Keep it up! {}{}".format(emoji,emoji),
                        "Nice one! {}{}".format(emoji,emoji),
                        "Rock on! {}{}".format(emoji,emoji),
                        "You're an inspiration to us all! {}{}".format(emoji,emoji),
                        "Wow! Such dedication! {}{}".format(emoji,emoji),
                        "Way to go! {}{}".format(emoji,emoji),
                        "I wish I had your energy! {}{}".format(emoji,emoji),
                        "Keep it going, we'll get there together! {}{}".format(emoji,emoji),
                        "No brakes on this train! {}{}".format(emoji,emoji),
                        "All aboard the fitnesstrain! Choo choo! {}{}".format(emoji,emoji)
                        ]
        comment = random.choice(commentlist)
        print("Commenting")
        commentfield = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/ul/li[{}]/div/div[4]/div/form/div/input[2]".format(i))
        commentfield.send_keys(comment)
        print(comment)
        time.sleep(1)
        commentfield.send_keys(Keys.RETURN)
        time.sleep(1)

    i += 1