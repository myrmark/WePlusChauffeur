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
    quoteslist = [
                    '"We cannot solve problems with the kind of thinking we employed when we came up with them." — Albert Einstein',
                    '"Learn as if you will live forever, live like you will die tomorrow." — Mahatma Gandhi',
                    '"Success is not final; failure is not fatal: It is the courage to continue that counts." — Winston S. Churchill',
                    '"The road to success and the road to failure are almost exactly the same." — Colin R. Davis',
                    '"It is better to fail in originality than to succeed in imitation." — Herman Melville',
                    '“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau',
                    '“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie',
                    '''"Nothing in the world can take the place of Persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan 'Press On' has solved and always will solve the problems of the human race." —Calvin Coolidge''',
                    '“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers',
                    '“Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden',
                    '“I never dreamed about success. I worked for it.” —Estée Lauder',
                    '“Success is getting what you want, happiness is wanting what you get.” ―W. P. Kinsella',
                    '“The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty." — Winston Churchill',
                    '“Don’t let yesterday take up too much of today.” — Will Rogers',
                    '“You learn more from failure than from success. Don’t let it stop you. Failure builds character.” — Unknown ',
                    '“If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you.” — Steve Jobs',
                    '“Experience is a hard teacher because she gives the test first, the lesson afterwards.” ―Vernon Sanders Law',
                    '“To know how much there is to know is the beginning of learning to live.” —Dorothy West',
                    '“Goal setting is the secret to a compelling future.” — Tony Robbins',
                    '''“Concentrate all your thoughts upon the work in hand. The sun's rays do not burn until brought to a focus. “ — Alexander Graham Bell''',
                    '“Either you run the day or the day runs you.” — Jim Rohn',
                    '“I’m a greater believer in luck, and I find the harder I work the more I have of it.” — Thomas Jefferson',
                    '“When we strive to become better than we are, everything around us becomes better too.” — Paulo Coelho',
                    '“Opportunity is missed by most people because it is dressed in overalls and looks like work.” — Thomas Edison',
                    '“Setting goals is the first step in turning the invisible into the visible.” — Tony Robbins',
                    '''“Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it.” — Steve Jobs''',
                    '“It’s not about better time management. It’s about better life management” — Alexandra of The Productivity Zone',
                    '“The elevator to success is out of order. You’ll have to use the stairs, one step at a time.” — Joe Girard',
                    '“Be a positive energy trampoline – absorb what you need and rebound more back.” — Dave Carolan',
                    '“People often say that motivation doesn’t last. Well, neither does bathing – that’s why we recommend it daily.” — Zig Ziglar',
                    '“Work until your bank account looks like a phone number.” — Unknown ',
                    '“I am so clever that sometimes I don’t understand a single word of what I am saying.” — Oscar Wilde',
                    '“People say nothing is impossible, but I do nothing every day.” — Winnie the Pooh',
                    '“Life is like a sewer… what you get out of it depends on what you put into it.” — Tom Lehrer',
                    '“I always wanted to be somebody, but now I realise I should have been more specific.” — Lily Tomlin',
                    ]
    quote = random.choice(quoteslist)
    image = random.choice(os.listdir(os.getcwd()+"\\images"))
    uploadimage = driver.find_element(by=By.CSS_SELECTOR, value="#new_attachment input[type=file]").send_keys(os.getcwd()+"\\images\\{}".format(image))
    time.sleep(10)
    textfield = driver.find_element(by=By.XPATH, value="""//*[@id="post_body"]""")
    textfield.send_keys(quote)
    time.sleep(1)
    input("test")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[3]/div[1]/div/div/form[2]/div/input").click()
    input("Press return to exit")
    driver.close()
    sys.exit()

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