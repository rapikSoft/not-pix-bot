from selenium.webdriver.common.by import By
from selenium import webdriver
import foo.openConfig as openConfig
import pyautogui
from time import sleep
class Bot:

    def __init__(self,browser, log) -> None:
        
        self.browser = browser
        self.logger = log
        self.claiming = False
        self.painting = False
        self.noEnergy = 0
        self.config = openConfig.getConfig()

    def claimCheck(self):

        if self.painting == False:
            self.claiming = True
            self.browser.find_element(By.CSS_SELECTOR,'div[style="transform: translateY(1px);"]').click()
            
            try:
                self.browser.find_element(By.CSS_SELECTOR,'button[style="font-family: arial; font-size: 17px;"]').click()
            except:
                 pass

            self.browser.find_element(By.CLASS_NAME,"_button_1cryl_1").click()


            self.claiming = False


        a = self.browser.find_element(By.CSS_SELECTOR,'div[style="transform: translateY(1px);"]').text.replace("\n","")
        self.logger.info("💰 Balance = "+ a)





    def paint(self):


        if self.claiming == False:

            
                self.painting = True
                self.browser.find_element(By.CLASS_NAME, "_button_hqiqj_147").click()
                self.painting = False


                a = self.browser.find_element(By.CSS_SELECTOR,'div[style="transform: translateY(1px);"]').text.replace("\n","")
                self.logger.info("💰 Balance = "+ a)


                



    def check(self, center):
        if self.browser.find_element(By.CLASS_NAME, "_button_text_hqiqj_171").text != "No energy":
            if list(pyautogui.screenshot().getpixel(((center[0], center[1])))) != [36,80,164]:

                self.paint()

        else:
            self.logger.info("⛔ No Enegry")
            self.noEnergy = 1




    def chooseColor(self):

            self.browser.find_element(By.CSS_SELECTOR , 'div[class*="_active_color_"]').click()


            sleep(0.3)
         
            self.browser.find_element(By.CSS_SELECTOR , 'div[style="background-color: rgb(36, 80, 164);"]').click()
   
        
            sleep(0.1)
            self.browser.find_element(By.CSS_SELECTOR , 'div[style="background-color: rgb(36, 80, 164);"]').click()
        