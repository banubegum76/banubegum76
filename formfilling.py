import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")
time.sleep(5)

#filling in the form
full_name = browser.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
full_name.send_keys("Banu Begum")

telephone = browser.find_element(By.XPATH, value= "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
telephone.send_keys("9148075555")

email = browser.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input ")
email.send_keys("banubegum76@gmail.com")

full_address = browser.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea")
full_address.send_keys("Biddapur Colony")

pin_code = browser.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input ")
pin_code.send_keys('585103')

DOB = browser.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input ")
DOB.send_keys("09/05/1994")

Gender = browser.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
Gender.send_keys('Female')

enter_code = browser.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
enter_code.send_keys("GNFPYC")

continue_button = browser.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
continue_button.click()

time.sleep(5)

#asserting that the browser title is correct
assert browser.title == "Your Account Has Been Created!"
time.sleep(5)
#closing the browser
browser.quit()