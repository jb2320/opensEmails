# #!/bin/env python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

EMAIL= 'drexel email'
PASSWORD = 'password123'
CHROMEPATH = ''



login_url = "https://learn.dcollege.net/"
browser = webdriver.Chrome()
browser.get(login_url)

#time.sleep(1)
browser.find_element_by_id("caslink1").click()
browser.implicitly_wait(3)
browser.find_element_by_id("username").send_keys(EMAIL)
#browser.find_element_by_id()
browser.find_element_by_id("password").send_keys(PASSWORD)
browser.find_element_by_name("_eventId_proceed").click()
browser.implicitly_wait(3)
browser.execute_script("window.open('https://one.drexel.edu/','drexelone')")
browser.implicitly_wait(3)
browser.execute_script("window.open('https://login.microsoftonline.com','microsoft email')")
browser.implicitly_wait(3)
EMAIL= 'email@drexel.edu'
browser.switch_to.window(browser.window_handles[1])
browser.find_element_by_name("loginfmt").send_keys(EMAIL)
browser.implicitly_wait(3)
browser.find_element_by_id("idSIButton9").click()
browser.implicitly_wait(3)
browser.find_element_by_id("i0118").send_keys(PASSWORD)
browser.implicitly_wait(3)


login_url = 'https://www.google.com/accounts/Login'

browser.get(login_url)
#for GMAIL
# EMAIL="email@gmail.com"
# PASSWORD="password123"
# browser.find_element_by_id("identifierId").send_keys(EMAIL)
# browser.find_element_by_id("identifierNext").click()
# time.sleep(.5)
# browser.find_element_by_name("password").send_keys(PASSWORD)
# browser.find_element_by_id("passwordNext").click()
# time.sleep(.5)

