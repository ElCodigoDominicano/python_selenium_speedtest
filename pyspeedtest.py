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

print("Welcome please wait while we set things up for you..")
driver: WebDriver = webdriver.Firefox()
print("driver has been set")
driver.get("https://www.speedtest.net/")
print("obtaining url")

try: 
    print("WebDriverWait 5 for element_to_be_clickable that element being a <div> with the class name 'start-text'")
    go_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
    )

    print("Going to click GO")
    go_button.click()
    print("clicked GO")

    print("going to wait 35 for speedtest to finish and target container holding test data.")
    time.sleep(40)
    # speedtest_container will contain all speedtest data.
    # it is grabbing element via its XML/XHTML XPath.
    speedtest_container = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]"))
    )
    
    download_speed = driver.find_element(By.CLASS_NAME, "download-speed")
    download_latency = driver.find_element(By.CLASS_NAME, "result-item-latencydown")
    ping_speed_ms = driver.find_element(By.CLASS_NAME, "ping-speed")
    upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed")
    result_data = driver.find_elements(By.CLASS_NAME, "result-data")
    # city_state = driver.find_element(By.CLASS_NAME, "js-sponser-name")
    # ip_addr = driver.find_element(By.CLASS_NAME, "js-data-ip")
    
    print()
    print(f"Download Speed: {download_speed.text}")
    print(f"Download Latency: {download_latency.text}")
    print(f"Upload Speed: {upload_speed.text}")
    # print(f"city_state: {city_state.text}")
    # print(f"IP Address: {ip_addr.text}")
    # print(f"Ping: {ping_speed_ms.text} ms")
    for element in result_data:
        print(element.text)
except Exception as e:
    print("The Exception caused couldve been a selenium issue (driver not loading), a network issue(website incorrect)", e)