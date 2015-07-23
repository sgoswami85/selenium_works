#!/usr/local/bin/python

""" This is module containing all test data necessary for our main script,
by using this we can upadte this file saperately without hard coding in our
main script """

# This is our base url
base_url = "https://www.gmail.com"
# gmail user name
my_username="shailesh.seleniumtest"
# password of gmail account
my_password="testTillBugDie"
# my email id 
my_email_id="shailesh.seleniumtest@gmail.com"
# 1st Receiver Email in To field
To_email_id="shailesh.goswami1985@gmail.com"
# 2nd Receiver email id in CC field
CC_email_id="shailesh.goswami85@gmail.com"
#3rd Receiver Email id in Bcc field for testing
BCC_email_id="shailesh.goswami85@gmail.com"

# Title of Base Url page for verification
base_url_title="Gmail"
#title of Inbox page
inbox_page_title=my_email_id+" - "+base_url_title  # to modify
# title of Sent Mail page
sent_mail_title="Sent Mail - shailesh.calsoft@gmail.com - Gmail"

#Message body (Considering we read this from a text file so every line we write in text file comes as different element in list in python)
body=["Name: Shailesh Goswami","Contact_No: +91-8451841481","Link to github:___"]
