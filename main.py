from colorama import Fore,init
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
import canvas
from _logging import getLogger
import subprocess
import psutil
import openConfig
import threading
from bot import bot
import pyautogui
import sys
import keyboard
init()



logger = getLogger()


# -Config Open-


config = openConfig.getConfig()



path = config["chrome"]["pathToChrome"]
profile = config["chrome"]["pathToProfile"]

logo = """
███╗░░██╗░█████╗░████████╗███╗░░██╗░█████╗░██████╗░███████╗
████╗░██║██╔══██╗╚══██╔══╝████╗░██║██╔══██╗██╔══██╗██╔════╝
██╔██╗██║██║░░██║░░░██║░░░██╔██╗██║██║░░██║██║░░██║█████╗░░
██║╚████║██║░░██║░░░██║░░░██║╚████║██║░░██║██║░░██║██╔══╝░░
██║░╚███║╚█████╔╝░░░██║░░░██║░╚███║╚█████╔╝██████╔╝███████╗
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░╚═════╝░╚══════╝"""

print(Fore.RED , logo, Fore.WHITE )



CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)




def closeChrome():
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "chrome.exe":
            try:

                proc.terminate()
            except:
                pass


closeChrome()
subprocess.Popen('chrome.exe --remote-debugging-port=9222  --disable-extensions --start-fullscreen', shell=True)


def checkChromeExit():
    while True:
        a = False
        for proc in psutil.process_iter():
            name = proc.name()
            if name == "chrome.exe":
                a = True
                break

        if a == False:
            logger.fatal("Chrome closed")
            close()


            
        




os.chdir(CURRENT_DIRECTORY)





def set_interval(func, sec):
    def func_wrapper():
        func()
        set_interval(func, sec)
        
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

#Main Code


def close():
    try:
        claimThread.join()
    except:
        pass

    try:
        colorCheckThread.join()
    except:
        pass
    closeChrome()
    logger.info("EXIT")
    sys.exit()

    



options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"

browser = webdriver.Chrome(options=options )
browser.get("https://web.telegram.org/k/#@notpixel")

sleep(1)

x = threading.Thread(target=checkChromeExit)
x.start()

#start web
while True:
    try:
        browser.find_element(By.CLASS_NAME, "is-view").click()
        break
    except:
        pass
        

try:
   
   browser.find_element(By.CLASS_NAME, "popup-button").click()

except:
    print(Fore.BLUE,"Btn `Launch` not found", Fore.WHITE)


sleep(3)

web = browser.find_element(By.TAG_NAME, "iframe")

browser.switch_to.frame(web)






#main 


canv = canvas.pixCanvas(browser)



canv.zoom(100)


bot = bot(browser, logger)

bot.claimCheck()
claimThread = set_interval(bot.claimCheck, 5*60)


pyautogui.moveTo((config["WIDTH"]/2)-20, config["HEIGHT"]/2)
pyautogui.click()


colorCheckThread = set_interval(bot.check, 5)


