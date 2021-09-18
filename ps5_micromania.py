from urllib.parse import uses_fragment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

import time
import random



def clickButton(find, by):
    try:
        WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((by, find))
        ).click()
    except Exception:
        clickButton(find, by)


def enterData(find, by, data):
    try:
        WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((by, find))
        ).send_keys(data)
        pass
    except Exception:
        enterData(find, by, data)



if __name__ == "__main__":
    
    email = "*****@****.com" 
    mdp = "***_**" 
    driver_path = "C:/Users/laith/dev/chromedriver_win32/chromedriver.exe" 

    software_names = [SoftwareName.BRAVE.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()

    option = webdriver.ChromeOptions()
    option.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument("window-size=1200,700")
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument("user-data-dir=selenium") 

    driver = webdriver.Chrome(executable_path=driver_path, options=option)
    driver.get('https://www.micromania.fr/')


    time.sleep(random.uniform(0.5, 1.9))

    class_name = "sidebar-login.header-link-item.icon-account.no-decoration.color-white"
    clickButton(class_name, By.CLASS_NAME)

    time.sleep(random.uniform(1.1, 2.8))

    enterData("email", By.NAME, email)
    time.sleep(random.uniform(1.3, 2.2))
    driver.find_element_by_name("password").send_keys(mdp)
    time.sleep(random.uniform(1.1, 1.8))
    driver.find_element_by_class_name("sc-htoDjs.evVIUk").click()
    
    time.sleep(random.uniform(1.5, 2.9))
    driver.get('https://www.micromania.fr/marvel-s-spider-man-miles-morales-107313.html')
    # print(driver.current_url)

    # clickButton("//*[@data-pid='107313']", By.XPATH)
    clickButton("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[3]/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[1]/button", By.XPATH)

    
    

    