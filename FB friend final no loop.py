# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 08:48:40 2017

@author: user
"""

'''
Scrapes the list of Friends of a given Facebook account and saves them in a .csv file.
'''

import codecs
import csv
import sys
import time
from getpass import getpass
from configparser import ConfigParser
from urllib.parse import urlparse
from lxml import html
#from wdstart import start_webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import urllib.request


class FacebookBot:
    def __init__(self):
        
        self.fbusername = '.......@gmail.com'
        self.fbpassword = '............'
        self.targeturl = 'https://www.facebook.com/julie.fievez/'
       
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
             'prefs', {
                 'credentials_enable_service': False,
                 "profile.default_content_setting_values.notifications" : 2,
                 'profile': {
                     'password_manager_enabled': False
                 }
             }
         )

        self.driver = webdriver.Chrome('C:\data\chromedriver.exe', chrome_options=chrome_options )
        WebDriverWait(self.driver, 10)
        
        #self.driver = start_webdriver('Chrome')

    def facebook_login(self):
        self.driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=111')
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "email")))
        self.driver.find_element_by_id('email').send_keys(".......@gmail.com")
        self.driver.find_element_by_id('pass').send_keys("..........")
        self.driver.find_element_by_id('loginbutton').click()

    def filter_url(self, x):
        elem = urlparse(x).path[1:]
        if elem == 'profile.php':
            elem = 'Not Available'
        return elem

    def scrape_friends(self):
        self.driver.get(self.targeturl)
        self.name = self.driver.title
        self.id = html.fromstring(self.driver.page_source.encode('utf-8')).xpath(
                    '//meta[@property="al:android:url"]/@content')[0][13:]
        self.username = self.filter_url(bot.driver.current_url)

        
        self.driver.get(self.targeturl + 'friends/')
        body = self.driver.find_element_by_tag_name('body')

        self.scroll(body)

        page = self.driver.page_source
        tree = html.fromstring(page.encode('utf-8'))

        #names = tree.xpath('//div[@id="collection_wrapper_2356318349"]//div[@class="fsl fwb fcb"]/a/text()')
        usernames = [self.filter_url(x) for x in
                     tree.xpath('//div[@id="collection_wrapper_2356318349"]//div[@class="fsl fwb fcb"]/a/@href')]
        #ids = [x[28:43] for x in
        #       tree.xpath('//div[@id="collection_wrapper_2356318349"]//div[@class="fsl fwb fcb"]/a/@data-hovercard')]

        self.data = (usernames)

    def scroll(self, body):
        num = 0
        count = 0

        while True:
            time.sleep(2)
            for i in range(40):
                body.send_keys(Keys.END)
            if not len(html.fromstring(self.driver.page_source.encode('utf-8')).xpath('//li[@class="_698"]')) > num:
                count += 1
            if count > 4:
                break
            num = len(html.fromstring(self.driver.page_source.encode('utf-8')).xpath('//li[@class="_698"]'))

    def save_data(self):
        with codecs.open(self.username + '.csv', mode='w', encoding='utf-8') as f:
            csvwriter = csv.writer(f)

            for i in range(len(self.data)):
                csvwriter.writerow([self.data[i]])

    def execute(self):

        self.facebook_login()
        self.scrape_friends()
        self.save_data()
        print('[*] List of friends saved as {}.csv'.format(self.username))
        self.driver.quit()


bot = FacebookBot()
bot.execute()