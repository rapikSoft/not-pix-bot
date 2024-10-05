from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class pixCanvas:

    def __init__(self, browser) -> None:
        
        
        self.browser = browser
        self.canv = self.browser.find_element(By.ID, "canvasHolder")
        self.zoomPlus = self.browser.find_elements(By.CLASS_NAME , "_button_dlzd9_17")[3]
        self.zoomMinus = self.browser.find_elements(By.CLASS_NAME , "_button_dlzd9_17")[4]
        self.action = ActionChains(self.browser)




    def zoom(self, x):


        for _ in range(x):

            self.zoomPlus.click()



