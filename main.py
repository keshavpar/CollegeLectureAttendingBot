from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException ,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec, wait
import time
from datetime import date
# import selenium
from model import courses 
#credentials
usernameSTR='21MCA2332'
passSTR='Parihar1@3'
#URLS 
url = 'https://cuchd.blackboard.com/'
browser=webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
  
browser.get(url)
browser.maximize_window()
browser.implicitly_wait(50)
#cookie and privacy policy
privacy = browser.find_element_by_class_name("button-1")
privacy.click()
#Login Page 
username = browser.find_element_by_id('user_id')
username.send_keys(usernameSTR)
pasword = browser.find_element_by_id('password')
pasword.send_keys(passSTR)
nextButton =browser.find_element_by_id('entry-login')
nextButton.is_enabled()
nextButton.click()
print('logged in success')


#2 page Courses names 


browser.implicitly_wait(10)
subject = browser.find_element_by_link_text(courses.AIP.value)
subject.click()

#Course
join=browser.find_element_by_id('sessions-list-dropXdown')

chapter=browser.find_element_by_class_name("js-description")
chapter.click()
# select = Select(join)
# #session
# try:
#     select.select_by_index(0)
#     browser.set_page_load_timeout(40*60)
#     browser.implicitly_wait(40)
# except NoSuchElementException:
#     print('No such Element found')    

# course=browser.find_element_by_link_text('Course Room')
# val=course.is_displayed()
# if(val==True):
#     course.click()   
#     browser.set_page_load_timeout(40*60)
#     browser.implicitly_wait(40)
#     toggle= browser.find_element_by_class_name('chevron-up-2pt')
#     toggle.click()
#     leave=browser.find_element_by_partial_link_text('session.actions.exit')
#     leave.click()
#     time.sleep(40*60)
# else:
#     browser.implicitly_wait(40*2)
