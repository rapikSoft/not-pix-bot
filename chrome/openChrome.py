import subprocess
import psutil
import sys
from foo import getLogger
from selenium import webdriver
from colorama import Fore
from time import sleep
from selenium.webdriver.common.by import By
def close():
    for proc in psutil.process_iter():
        
            try:
                name = proc.name()
                if name == "chrome.exe":

                    proc.terminate()
            except:
                pass


def open(config,acc):
    #close()
    
    subprocess.Popen(f'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port={config["port"]}  --disable-extensions --profile-directory="{acc}" https://web.telegram.org/k/#@notpixel', shell=True)

    

    return iframe(connect(config["port"]))


def iframe(browser):
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


    return browser



def checkChromeExit(func):
    while True:
        a = False
        for proc in psutil.process_iter():
            name = proc.name()
            if name == "chrome.exe":
                a = True
                break

        if a == False:
            getLogger().fatal("Chrome closed")   
            func()



def connect(port):


    options = webdriver.ChromeOptions()
    options.debugger_address = "127.0.0.1:"+str(port)

    browser = webdriver.Chrome(options=options )
    browser.set_window_size(100,600)
    browser.set_window_rect(-10,0)


    

    return browser
