import discord
import os
import requests
import json
import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def joinclass(var):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")

    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0, 
    "profile.default_content_setting_values.notifications": 1 
    })

    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\praka\Downloads\chromedriver_win32\chromedriver.exe')

    classes=var

    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(5)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("prakashsewani001@gmail.com")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@name='password']").send_keys("omsairam1994")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
    driver.get(classes)
    driver.refresh()
    time.sleep(8)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(2)
    driver.find_element_by_xpath("//span[contains(text(),'Ask to join')]").click()
    time.sleep(60*49)
    driver.close()

def rejoinclass(var):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")

    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0, 
    "profile.default_content_setting_values.notifications": 1 
    })

    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\praka\Downloads\chromedriver_win32\chromedriver.exe')

    classes=var

    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(5)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("prakashsewani001@gmail.com")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@name='password']").send_keys("omsairam1994")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
    driver.get(classes)
    driver.refresh()
    time.sleep(8)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("tab", do_press=True, do_release=True)
    keyboard.send("enter", do_press=True, do_release=True)
    time.sleep(2)
    driver.find_element_by_xpath("//span[contains(text(),'Join now')]").click()
    time.sleep(60*51)
    driver.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='$help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$qoute'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('join CSSMORE'):
        subject="https://meet.google.com/nqp-eyaf-ngr"
        await message.channel.send("Joining C$SS More Sir's Lecture Now")
        joinclass(subject)
    
    if message.content.startswith('join SE'):
        subject="https://meet.google.com/ixa-nyfo-cjz"
        await message.channel.send("Joining SE Naveen Sir's Lecture Now")
        joinclass(subject)

    if message.content.startswith('rejoin SE'):
        subject="https://meet.google.com/ixa-nyfo-cjz"
        await message.channel.send("Rejoining SE Naveen Sir's Lecture Now")
        rejoinclass(subject)
    
    if message.content.startswith('join SPCC'):
        subject="https://meet.google.com/kod-kkzi-dsu"
        await message.channel.send("Joining SPCC Moushmee Madam's Lecture Now")
        joinclass(subject)
    
    if message.content.startswith('rejoin SPCC'):
        subject="https://meet.google.com/kod-kkzi-dsu"
        await message.channel.send("Rejoining SPCC Moushmee Madam's Lecture Now")
        rejoinclass(subject)

    if message.content.startswith('join CSSUMA'):
        subject="https://meet.google.com/ykj-wzfj-ybz"
        await message.channel.send("Joining C$SS Uma Madam's Lecture Now")
        joinclass(subject)

    if message.content.startswith('rejoin CSSUMA'):
        subject="https://meet.google.com/ykj-wzfj-ybz"
        await message.channel.send("Rejoining C$SS Uma Madam's Lecture Now")
        rejoinclass(subject)

    if message.content.startswith('join DWM'):
        subject="https://meet.google.com/szx-ctjs-ero"
        await message.channel.send("Joining DWM Ranjana Madam's Lecture Now")
        joinclass(subject)

    if message.content.startswith('rejoin DWM'):
        subject="https://meet.google.com/szx-ctjs-ero"
        await message.channel.send("Rejoining DWM Ranjana Madam's Lecture Now")
        rejoinclass(subject)
    
    if message.content.startswith('$help'):
        await message.channel.send("Commands to help navigate me!")
        await message.channel.send("join <LECTURE NAME>")
        await message.channel.send("rejoin <LECTURENAME>")
        await message.channel.send("<LECTURE NAME> all caps :)")
    
    if message.content.startswith('$help easteregg'):
       await message.channel.send("Try $qoute ;)") 

client.run('ODIwMzcyNTUyMTM5OTMxNjg4.YE0Neg.-HICiM7FYgCUKP1nTKwdS2FD6zk')