from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class PortailCo:
    
    def __init__(self, email, mdp, driver_path):
        self.email = email 
        self.mdp = mdp 
        option = webdriver.ChromeOptions()
        option.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        self.driver.get('https://www.leonard-de-vinci.net/')

        logusr = self.driver.find_element_by_id("login")
        logusr.send_keys(self.email)
        logusr.send_keys(Keys.RETURN)

        try:
            logmdp = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "passwordInput"))
            )
            logmdp.send_keys(self.mdp)
            logmdp.send_keys(Keys.RETURN)
        except:
            pass
        
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div[1]/a[2]').click()




if __name__ == "__main__":
    personal_info = dict(
        email = "***.*****@edu.devinci.fr", 
        mdp = "*******", 
        driver_path = "C:/Users/laith/dev/chromedriver_win32/chromedriver.exe" 
    )
    
    bot = PortailCo(**personal_info)
    
    

    