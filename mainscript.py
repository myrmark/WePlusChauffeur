#Author Filip Malmberg

import os
import sys
import ctypes
import time
import subprocess
import platform
import random
import getpass

from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

emoji = u'\U0001F44D'

email = input("Enter your email: ")
password = getpass()

driver = webdriver.Firefox()
driver.get('https://weplusapp.com')
driver.implicitly_wait(20)
logincheck = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/form/div[3]/a[1]"))).text
if logincheck:
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    email.send_keys(email)
    password.send_keys(password)
    loginbutton = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/form/div[3]/input").click()
driver.implicitly_wait(20)
time.sleep(3)
companybutton = driver.find_element(by=By.XPATH, value="/html/body/ul[1]/li[2]/a")
companybutton.click()
driver.implicitly_wait(20)
time.sleep(3)
select = Select(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/div/form/div[1]/div[1]/div/select"))
select.select_by_value("created-at")
driver.implicitly_wait(20)
time.sleep(3)
selectall = Select(driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/div/form/div[1]/div[2]/div/select"))
selectall.select_by_value("all")
driver.implicitly_wait(20)
time.sleep(3)
i = 1
while True:
    if i == 7 or i == 13 or i == 19 or i == 25 or i == 31 or i == 37 or i == 43 or i == 49 or i == 55 or i == 61:
        morebutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[4]/div/ul/li[{}]/a".format(i)).click()
        driver.implicitly_wait(20)
    time.sleep(3)
    postpath = "/html/body/div[2]/div[4]/div/ul/li[{}]".format(i)
    post = driver.find_element(by=By.XPATH, value=postpath).click()
    driver.implicitly_wait(20)
    time.sleep(3)
    try:
        likebutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/ul/li/div/ul/li/a")
    except Exception:
        continue
    if not likebutton:
        driver.close()
        break
    else:
        likebutton.click()
    time.sleep(3)
    namefield = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/ul/li/div/div[1]/div/h3/strong"))).text
    name = namefield.split(' ')[0]
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
    commentfield = driver.find_element(by=By.XPATH, value="""//*[@id="comment_body"]""")
    commentfield.send_keys(comment)
    time.sleep(3)
    commentfield.send_keys(Keys.RETURN)
    time.sleep(3)
    xbutton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/a").click()
    time.sleep(3)
    i += 1