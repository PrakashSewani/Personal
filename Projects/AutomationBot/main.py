from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import keyboard
import datetime
import time
import signal
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed

message1='<@438447686673235968> the AutomationBot is Online'
message2='<@438447686673235968> The Lecture Has Started!'
message3='<@438447686673235968> The Suffering Has Ended'
webhook1=DiscordWebhook(url='https://discord.com/api/webhooks/818166080316112907/G9ODme6zL5LWRyEwjv7K1C1Du0LZSm8wWSb2jhq7t3Ovk_ctQhnzI3iU9dA0Rd8dCVzC',username='OPBot',content=message1)
embed=DiscordEmbed(title='**Pro Gamer Move Executed**')
embed.set_timestamp()

webhook1.add_embed(embed)
respond=webhook1.execute()

t_end = time.time() + 60 * 60 * 7
while time.time() < t_end:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    justtime = now.strftime("%H:%M")
    print (current_time)

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

    while justtime !=  "09:32" or justtime != "10:32" or justtime != "11:32" or  justtime != "12:32" or justtime != "13:02" or justtime != "14:32":
        time.sleep(20)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M / %A")
        justtime = now.strftime("%H:%M")
        print(justtime)
        if justtime !=  "09:32" or justtime != "10:32" or justtime != "11:32" or  justtime != "12:32" or justtime != "13:02" or justtime != "14:32":
            print("Class is going to start in 10 Minutes.")
            break
        
    def gmail_login():
        
        webhook2=DiscordWebhook(url='https://discord.com/api/webhooks/818166080316112907/G9ODme6zL5LWRyEwjv7K1C1Du0LZSm8wWSb2jhq7t3Ovk_ctQhnzI3iU9dA0Rd8dCVzC',username='OPBot',content=message2)
        respond2=webhook2.execute()

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
    
        driver.get(sub)
        driver.refresh()
        time.sleep(8)
        
        """
        #Turn off Mic
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(2)
        
        #Turn off Camera
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(5)
        """

        driver.find_element_by_xpath("//span[contains(text(),'Ask to join')]").click()
        time.sleep(60*55)
        webhook3=DiscordWebhook(url='https://discord.com/api/webhooks/818166080316112907/G9ODme6zL5LWRyEwjv7K1C1Du0LZSm8wWSb2jhq7t3Ovk_ctQhnzI3iU9dA0Rd8dCVzC',username='OPBot',content=message3)
        respond3=webhook3.execute()
        driver.close()

    # DWM
    if current_time == "09:32 / Monday" or current_time == "10:32 / Tuesday" or current_time == "09:32 / Wednesday" or current_time == "10:32 / Thursday" :
        sub = "https://meet.google.com/szx-ctjs-ero"
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\praka\Downloads\chromedriver_win32\chromedriver.exe')
        gmail_login()
        
    # SE 
    elif current_time == "10:32 / Monday" or current_time == "09:32 / Tuesday" or current_time == "10:32 / Wednesday" or current_time == "09:32 / Thursday":
        sub = "https://meet.google.com/ixa-nyfo-cjz"
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\praka\Downloads\chromedriver_win32\chromedriver.exe')
        gmail_login()
            
    # C&SS
    elif current_time == "14:01 / Monday" or current_time == "15:01 / Tuesday" or current_time == "15:01 / Thursday" or current_time == "09:31 / Friday":
        sub = "https://meet.google.com/ykj-wzfj-ybz"
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\praka\Downloads\chromedriver_win32\chromedriver.exe')
        gmail_login()
        
    # SPCC
    elif current_time == "15:01 / Monday" or current_time == "14:01 / Tuesday" or current_time == "14:01 / Thursday" or current_time == "10:31 / Friday":
        sub = "https://meet.google.com/kod-kkzi-dsu"
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\praka\Downloads\chromedriver_win32\chromedriver.exe')
        gmail_login()

    else:
        print("No classes right now")