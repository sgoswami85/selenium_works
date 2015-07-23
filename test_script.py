#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, datetime
import test_data

class TestGmail(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome('C:\Users\shailesh.goswami\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver=webdriver.Firefox()
        print "|Browser started.."
        self.driver.implicitly_wait(10)
            
    def test_LogIn(self):
        self.driver.get(test_data.base_url)
        actualTitle=self.driver.title
        if actualTitle==test_data.base_url_title:
            print "|Gmail Home page Load: PASSED"
        else:
            print "|Gmail Home page Load: FAILED"
        print "|Entering Username.."
        self.driver.find_element_by_xpath("//input[@id='Email']").send_keys(test_data.my_username)
        self.driver.find_element_by_id("next").click()
        print "|Entering Password.."
        self.driver.find_element_by_xpath("//input[@id='Passwd']").send_keys(test_data.my_password)
        pers_checkbox_status=self.driver.find_element_by_xpath("//input[@id='PersistentCookie']").is_selected()
        if pers_checkbox_status == True:
            self.driver.find_element_by_xpath("//input[@id='PersistentCookie']").click()
        self.driver.find_element_by_xpath("//input[@id='signIn']").click()

        #--wait for logged in status---
        
        #---Wait and Check for Inbox page load ---
        print "|waiting for Email Inbox page load completely.."
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@gh='cm']")))    #checking for Compose button presence
        print "|Verifying Inbox Page load.."
        actualTitle=self.driver.title
        if test_data.inbox_page_title in actualTitle:
            print "|Gmail Inbox Page Load: PASSED"
        else:
            print "|Gmail Inbox Page Load: FAILED"
        #--- Compose Email ---
        print "|Composing New Email.."
        self.driver.find_element_by_xpath("//div[@gh='cm']").click()    #click compose button
        self.driver.find_element_by_xpath("//textarea[contains(@aria-label,'To')]").send_keys(test_data.To_email_id)  # text box of "TO"
        self.driver.find_element_by_xpath("//span[@aria-label='Add Cc Recipients ‪(Ctrl-Shift-C)‬']").click() # add cc
        self.driver.find_element_by_xpath("//textarea[@aria-label='Cc']").send_keys(test_data.CC_email_id) # text box of "CC"
        self.driver.find_element_by_xpath("//span[@aria-label='Add Bcc Recipients ‪(Ctrl-Shift-B)‬']").click()
        self.driver.find_element_by_xpath("//textarea[@aria-label='Bcc']").send_keys(test_data.BCC_email_id) # text box of "CC"

        #--- Write Message Body ---
        for i in range(len(test_data.body)):
            self.driver.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(test_data.body[i]+"\n")
  
        #-- To include some uniqueness in every Email to be Sent for later verification (optional feature) ---
        time_stamp_temp=datetime.datetime.now()
        time_stamp=str(time_stamp_temp)
        subject_reference_text="selenium_assignment: Timestamp::"+time_stamp # use this for comparison of mail sent and received
        self.driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys(subject_reference_text)  # write something in subject

        #--- Send Email ---
        print "|Sending Email.."
        self.driver.find_element_by_xpath("//div[@aria-label='Send ‪(Ctrl-Enter)‬']").click()   #click on Send button

        #--- wait till Email is being sent ---
        print "|waiting while Email is being sent.. "
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(.,'Your message has been sent. View message')]")))
        #time.sleep(10)
        



    def tearDown(self):
        self.driver.quit()       

if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit:
        pass
