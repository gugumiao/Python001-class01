#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver

# 83.0.4103.39/chromedriver_mac64
user = '13164146813'
passwd = 'geektime'

browser = webdriver.Chrome()
browser.get('https://shimo.im/login?from=home')
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(user)
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(passwd)
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

