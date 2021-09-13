# -*- coding: utf-8 -*-
"""
Created on Fri May  7 00:45:36 2021

@author: jared
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from playsound import playsound
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from win32com.client import Dispatch
from twilio.rest import Client
    
def chrome_setup():
    print("Setting up Chrome driver...")
    global options
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    global chrome_path
    chrome_path = r"C:\Users\jared\documents\STONKS\chromedriver.exe"
    print("Chrome driver ready.")
    browser_start()

def browser_start():
    global target
    print("Starting each browser...")
    target = webdriver.Chrome(executable_path = chrome_path, options = options)
    print("Target ready.")
    page_load()

def page_load():
    target_url = "https://www.target.com/p/neutrogena-ultra-sheer-lightweight-sunscreen-spray-spf-100-5oz/-/A-52542750#lnk=sametab"
    target.get(target_url)
    #assigns the correct link to each browser
    time.sleep(2)
    init_status()

def init_status():
    global target_status
    target_status = target.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div/div")
    target_status = target_status.text
    
    try:
        target_status = target.find_element_by_xpath("//button[@data-test='orderPickupButton']")
        target_status = target_status.text
        print(target_status)
    except NoSuchElementException:
        print("DNE")
    
chrome_setup()