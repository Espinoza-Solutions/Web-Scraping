from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
#main
def main():
    
    print("which of the SEQ you want looking for? ")
    #SEQ_number = input()
    file_name = r'c:\Users\ZizhouHe\Desktop\TEST\TEST.xlsx'
    data = pd.read_excel(file_name)
    print(data['SEQ'])

#check status
#main()
def checkStatus():
    driver = webdriver.Chrome('C:\\Users\\ZizhouHe\\Desktop\\TEST\\chromedriver.exe')
    driver.get("https://connect.ota.here.com/#/device/30201586-4432-43f9-b653-d8792b234c9c")
    time.sleep(3)

    user = driver.find_element_by_id("sign-in-email")
    ps = driver.find_element_by_id("sign-in-password-encrypted")
    sub = driver.find_element_by_id("signInBtn")
    user.send_keys('')
    ps.send_keys("")
    time.sleep(1)
    sub.click()
    time.sleep(10)
    driver.get("https://connect.ota.here.com/#/device/18d73763-0c62-42f3-b35f-eb1791864c03")
    time.sleep(2)
    install_found = driver.find_element_by_xpath('//div[text()= "Installation pending"]')
    install_found.click()
    time.sleep(5)

    downS = driver.find_element_by_id("download-start-time").get_attribute('innerText')
    downC = driver.find_element_by_id("download-completed-time").get_attribute('innerText')
    inS = driver.find_element_by_id("queued-packages").get_attribute('innerText')

    z = str(inS)
    x = z.split("\n")
    check = x[-8:]
    PN = 0
    for i in check:
        if i =='Pending':
            PN +=1

    if PN == 1:
        print("installing")
    if PN == 2:
        print("ready to consent")
    if PN == 3:
        print("downeloading")

    time.sleep(2)
    driver.close()

checkStatus()