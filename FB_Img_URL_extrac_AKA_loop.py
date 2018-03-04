# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:57:53 2018

@author: user
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request

# Main conect to Facebook
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

driver = webdriver.Chrome('C:\data\chromedriver.exe', chrome_options=chrome_options )
wait = WebDriverWait(driver, 10)
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=111')
wait.until(EC.visibility_of_element_located((By.ID, "email")))
driver.find_element_by_id('email').send_keys(".......@gmail.com")
driver.find_element_by_id('pass').send_keys("..........")
driver.find_element_by_id('loginbutton').click()


# ### Get the profile photo from the FB page of someone and store the 
# image in the directory of the programm in jpg format
i=1
fin = open("julie.fievez.csv",'r',encoding = 'utf-8')
fout = open("julie.fievez2.csv",'w',encoding = 'utf-8')
for line in fin :   
    if line != 'Not Available':
        driver.get('https://www.facebook.com/'+line)
        PP=driver.find_elements_by_class_name("profilePicThumb")
        if len(PP) !=0:
            urlphoto=(PP[0].get_attribute("href"))
            driver.get(urlphoto)
            Laphoto=driver.find_elements_by_class_name("spotlight")
            ii=urlphoto.find("e_id=")
            eid=urlphoto[ii+5:len(urlphoto)]
            ii=urlphoto.find("e_id=")
            eid=urlphoto[ii+5:len(urlphoto)]
            # urllib.request.urlretrieve('https://graph.facebook.com/'+eid+'/picture?width=9999&height=9999',"c:\PhotoFB\photoFBG"+eid+".png")    
            fout.write(line[:-1]+","+eid+"\n")
            
            i+=1
            if i>50 : break
         
fin.close()
fout.close()
# quit the browse
driver.quit()

