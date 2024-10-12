from colorama import Fore,init
from time import sleep
from selenium.webdriver.common.by import By
from foo import pixCanvas
from foo import getLogger
from foo import getConfig,getAccaunts
import threading
from bot import Bot
from random import randint
import pyautogui

import chrome
import sys
init()

logger = getLogger()


# -Config Open-


config = getConfig()




logo = """

╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋┏━┳┓
╋╋╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋╋╋╋┃┏┛┗┓
┏━┳━━┳━━┳┫┃┏┓┏━━┳━━┳┛┗┓┏┛
┃┏┫┏┓┃┏┓┣┫┗┛┛┃━━┫┏┓┣┓┏┫┃
┃┃┃┏┓┃┗┛┃┃┏┓┓┣━━┃┗┛┃┃┃┃┗┓
┗┛┗┛┗┫┏━┻┻┛┗┛┗━━┻━━┛┗┛┗━┛
╋╋╋╋╋┃┃
╋╋╋╋╋┗┛"""

print(Fore.RED , logo, Fore.WHITE )
print("Creators: https://t.me/+RUoqZfYRYIs0NDc0")
















def set_interval(func, sec):
    def func_wrapper():
        func()
        set_interval(func, sec)
        
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

#Main Code


def close():

    claimThread.cancel()



    colorCheckThread.cancel()

    chrome.close()
    logger.info("EXIT")
    sys.exit()

    












#main 
mainProfiles = config["chrome"]["mainProfiles"]
if mainProfiles == False:

    

    acc = getAccaunts(config["chrome"]["pathToProfiles"]+"\\Local State")

else:
    acc = getAccaunts(config["chrome"]["pathToProfiles"]+"\\Local State",config["chrome"]["profiles"])
    accIndex = 0
    presentAcc = acc[accIndex]
   


print("🙉 Your Profiles:")
for a in acc:

    print(a)




def init_(acc):


    chrome.close()
    browser = chrome.open(config,acc)



    seed = 0
    while True:
        try:
            canv = pixCanvas(browser)
            seed = 0
            break
        except:
            seed += 1


            if seed >3000:
                seed = 0
                chrome.close()
                browser = chrome.open(config)
                

    windowCenter= [(browser.get_window_position()["x"]+browser.get_window_size()["width"]+10)//2, browser.get_window_position()["y"]+browser.get_window_size()["height"]//2]

    canv.zoom(10)


    bot = Bot(browser, logger)

    bot.claimCheck()
    claimThread = set_interval(bot.claimCheck, 5*60)
    logger.info(f"🪟 {browser.get_window_position()}")

    pyautogui.moveTo(windowCenter[0]-10,windowCenter[1])
    pyautogui.click()



    bot.chooseColor()


    colorCheckThread = set_interval(lambda: bot.check(windowCenter), 5)

    return bot,claimThread,colorCheckThread

bot,claimThread,colorCheckThread = init_(acc if mainProfiles==False else presentAcc)
if mainProfiles:
    
    accIndex += 1
    try:
        presentAcc = acc[accIndex]
    except:
        accIndex +=1
while True:
    if mainProfiles == False:
        if bot.noEnergy == 1:
            try:
                claimThread.cancel()
            except:
                pass

            try:
                colorCheckThread.cancel()
            except:
                pass
            chrome.close()
            time_ = int(config["SLEEP_TIME"])
            logger.info(f"💤 launch in {time_/60} min")
            sleep(time_)

            bot,claimThread,colorCheckThread = init_(acc)
    else:
        if bot.noEnergy == 1:
            try:
                claimThread.cancel()
            except:
                pass

            try:
                colorCheckThread.cancel()
            except:
                pass
            chrome.close()
            time_ = randint(1,10)
            logger.info(f"💤 next profile  launch in {time_} sec")
            sleep(time_)

            bot,claimThread,colorCheckThread = init_(presentAcc)
            accIndex += 1
            try:
                presentAcc = acc[accIndex]
            except:
                chrome.close()

                accIndex = 0
                presentAcc = acc[accIndex]
                time_ = int(config["SLEEP_TIME"])
                logger.info(f"💤 launch in {time_/60} min")
                sleep(time_)


                bot,claimThread,colorCheckThread = init_(presentAcc)