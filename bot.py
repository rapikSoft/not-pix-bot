from selenium.webdriver.common.by import By
import openConfig
import pyautogui

class bot:

    def __init__(self,browser, log) -> None:
        
        self.browser = browser
        self.logger = log
        self.claiming = False
        self.painting = False

        self.config = openConfig.getConfig()

    def claimCheck(self):
        if self.painting == False:
            self.claiming = True
            self.browser.find_element(By.CLASS_NAME,"_button_tksty_1").click()


            self.browser.find_element(By.CLASS_NAME, "_container_3i6l4_1").click()

            self.browser.find_element(By.CLASS_NAME,"_button_1cryl_1").click()


            self.claiming = False





    def paint(self):


        if self.claiming == False:

            
                self.painting = True
                self.browser.find_element(By.CLASS_NAME, "_button_hqiqj_147").click()
                self.painting = False


                



    def check(self):
        if self.browser.find_element(By.CLASS_NAME, "_button_text_hqiqj_171").text != "No energy":
            if list(pyautogui.screenshot().getpixel(((self.config["WIDTH"]/2)-20, self.config["HEIGHT"]/2))) != [0,0,0]:

                self.paint()

        else:
            self.logger.info("No Enegry")
