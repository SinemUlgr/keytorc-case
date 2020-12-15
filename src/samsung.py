from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
driver=webdriver.Chrome(executable_path="C:\\Users\\sinem.ulger\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get('https://www.n11.com/')
time.sleep(1)
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="userKvkkModal"]/div/div[2]/span').click()
search_input=driver.find_element_by_id('searchData')
search_input.send_keys('samsung')
time.sleep(1)
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/div[1]/a/span').click()
time.sleep(1)
output_count = int(''.join(filter(str.isdigit, driver.find_element_by_xpath('//*[@id="itemCount"]').get_attribute('value'))))
if output_count > 0:
    print(output_count)
    print("SONUÇ VAR")
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="contentListing"]/div/div/div[2]/div[5]/a[2]').click()
time.sleep(1)
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="p-388616798"]/div[1]/span').click()
time.sleep(3)
driver.quit()