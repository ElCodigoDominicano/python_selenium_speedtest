"""
    need to click "Go"
    the "Go"'s element is in a: <span class="start-text"></span>
    
    need to obtain the information stored in element
    <div class=speedtest-container main-row> </div>
    the above element grabs the data of the speed test
    
    <div class="guage-speed-needle">
"""
import time
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL: str = 'https://www.speedtest.net'
print("Welcome please wait while we set things up for you..")
driver: WebDriver = webdriver.Firefox()
print(f"driver has been set, opening webpage {URL}.")
driver.get("https://www.speedtest.net/")

try:
    # the GO button is in this tag => <span class="start-text"></span>
    print("WebDriverWait 5 for element_to_be_clickable that element being a <div> with the class name 'start-text'")
    go_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
    )

    print("Going to click GO")
    go_button.click()
    print("clicked GO")

    print("going to wait 40 for speedtest to finish and target container holding test data.")
    time.sleep(40)
    # The speedtest data is in this tag => <div classnamw='speedtest_container'>
    # it is grabbing element via its XML/XHTML XPath.
    speedtest_container = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]"))
    )
    
except Exception as e:
    print("The Exception caused couldve been a selenium issue (driver not loading), a network issue(website incorrect)", e)
