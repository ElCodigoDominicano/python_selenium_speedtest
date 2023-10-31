"""
    need to click "Go"
    the "Go"'s element is in a: <span class="start-text"></span>
    
    need to obtain the information stored in element
    <div class=speedtest-container main-row> </div>
    the above element grabs the data of the speed test

    the element below contains the speedtest RPM guage
    <div class="guage-speed-needle">

    a simple speedtest bot using selenium 
    @elcodigodominicano
"""
import time
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Welcome, please wait while we set things up for you..")
URL: str = 'https://www.speedtest.net'
driver: WebDriver = webdriver.Firefox()

print(f"driver has been set, opening webpage {URL}.")
driver.get("https://www.speedtest.net/")

try:
    # the GO button is in this tag => <span class="start-text"></span>
    print("WebDriverWait 5 for element_to_be_clickable, that element being a <span> tag with the class name 'start-text'")
    go_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
    )

    print("Going to click GO")
    go_button.click()
    print("clicked GO")
    
    print("going to Sleep for 40-seconds to let speed-test finish")
    time.sleep(40)
    
    # The speedtest data is in this tag => <div classname='speedtest_container'>
    # it is grabbing element via its XML/XHTML XPath.
    # prints out all data containing the speedtest_container
    speedtest_container = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]"))
    )
    print(speedtest_container.text)
    
except Exception as e:
    print("The Exception caused could've been a selenium issue (driver not loaded, version different), a network issue(website incorrect)", e)
