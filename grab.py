import sys
import paramiko
sys.stderr = sys.__stderr__
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from random import choice
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent
import csv
from faker import Faker
from faker.providers import person
import random
import string
from time import sleep as wait
import sys
from pyvirtualdisplay import Display
import json
from urllib.request import urlretrieve
import requests
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
import time
import os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from colorama import Fore, Back, Style 
from colorama import init
init()

acToken = "f01adfb276c573b84d2f206685c22a38"

def login_labs(email,passwd,empas):
    try:
        output = ""
        global driver
        print("Azure VM Labs Grabber Bot by Riskids")
        print("Grabbing new account...")
        
        email = email.replace(" ", "")
        myproxy = get_proxy()
        
        # prox = Proxy({
        #     'proxyType': ProxyType.MANUAL,
        #     'httpProxy': myproxy,
        #     'ftpProxy': myproxy,
        #     'sslProxy': myproxy,
        #     'noProxy': '' # set this value as desired
        #     })
        pieces = myproxy.split(":")
        host = pieces[0]
        port = pieces[1]
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", UserAgent().random)
        print("use proxy ", myproxy)


       # firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
       # firefox_capabilities['marionette'] = True
       # firefox_capabilities['proxy'] = {
       #     "proxyType": "MANUAL",
       #     "httpProxy": myproxy,
       #     "ftpProxy": myproxy,
       #     "sslProxy": myproxy,
       #     }
        
        print("use user-agent: ", UserAgent().random)
        driver = webdriver.Firefox(executable_path='../drivers/geckodriver',firefox_profile=profile) 
        driver.get(invite_url)
        if is_visible("i0116",90) is True:
           pass
        wait(1)
        driver.find_element_by_id("i0116").send_keys(email)
        wait(0.5)
        driver.find_element_by_id("idSIButton9").click()
        if is_visible("i0118",60) is True:
            pass
        driver.find_element_by_id("i0118").send_keys(passwd)
        wait(0.5)
        driver.find_element_by_id("idSIButton9").click()
        wait(2)
        if is_visible("iShowSkip",0.5) is True:    
            driver.find_element_by_id("iShowSkip").click()
            wait(2)
            print("akun warning!")

        if is_visible("idBtn_Back",2) is True:    
            driver.find_element_by_id("idBtn_Back").click()
            print("stay signed? skipping...")    
        if is_visible("iCancel",1) is True:    
            driver.find_element_by_id("iCancel").click()
            print("password break, skipping...")            
                
        if is_locked() is True:
            driver.find_element_by_class_name("salah bos").click()               
        if is_visible_switch() is True:
            print("logging in.....")
            print("labs loaded....")
            print("Vm Grabbed, Clossing...")
            driver.quit()        
            return True
        else:
            driver.find_element_by_class_name("Request Time Out Bro").click() 
            print("RTO BOSS")
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        driver.quit()   
        return False

def is_visible(locator, timeout):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
        return True
    except TimeoutException:
        return False

def is_visible_captcha(timeout=20):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "forVisualHip"))) 
        return True
    except TimeoutException:
        return False

def is_locked(timeout=5):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "StartAction"))) 
        return True
    except TimeoutException:
        return False        

def is_visible_switch(timeout=120):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, "ms-Toggle-background"))) 
        return True
    except TimeoutException:
        return False

def get_proxy():
    with open("proxy.txt") as f:
        proxies = f.readlines()
        proxy = random.choice(proxies)
        return proxy

#=============== perintah utama ==================#
with open("lab.txt","r") as f:
    count_lab = 0
    for line in f :
        invite_url = line
        print("grabbing account with link "+invite_url)
        with open("accLogin_1.txt", 'r') as f:
            count = 0
            for line in f:
                if count < 5:
                    i = 0
                    while i < 2:
                        print("FAST AZURE LABS GRABBER. by riskids")
                        pieces = line.split(":")
                        email = pieces[0]
                        passwd = pieces[1]
                        is_login = login_labs(email,"pepengkolan1",line)
                        if is_login is True:
                            print(Back.GREEN+"Grab Account Done")
                            print(Style.RESET_ALL)
                            print("With Account : ",email)
                            count += 1
                            print("Total Account Grabbed: ",count)
                            break
                        else:
                            print(Back.RED+"TERJADI ERROR, MENGULANGI LOGIN")
                            print(Style.RESET_ALL)
                            print("Total Grabbed: ",count)
                            continue
                    continue
                else:
                    break    
        count_lab += 1
        print(Back.GREEN+"link ke "+str(count_lab)+" done")      
        print(Style.RESET_ALL)  