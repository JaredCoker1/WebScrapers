# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 18:29:18 2021

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

global speak
speak = Dispatch("SAPI.SpVoice").Speak
    
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
    global bby 
    global target
    global ms
    print("Starting each browser...")
    bby = webdriver.Chrome(executable_path = chrome_path, options = options)
    print("Bestbuy ready.")
    target = webdriver.Chrome(executable_path = chrome_path, options = options)
    print("Target ready.")
    ms = webdriver.Chrome(executable_path = chrome_path, options = options)
    print("Microsoft ready.")
    #opens chrome browser for each website
    print("All browsers ready.")
    page_load()

def page_load():
    bby_url = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
    bby.get(bby_url)  
    target_url = "https://www.target.com/p/xbox-series-x-console/-/A-80790841"
    target.get(target_url)
    ms_url = "https://www.xbox.com/en-us/configure/8wj714n3rbtl"
    ms.get(ms_url)
    print("All browsers loaded.")
    #assigns the correct link to each browser
    time.sleep(2)
    infinite_check()

def infinite_check():
    global bby_status
    global target_status
    global ms_status

    bby.execute_script("window.scrollTo(0, 700)") 
    i = 0
    
    while i<1:
        try:
            bby_status = bby.find_element_by_xpath("//button[@class='btn primary']")
            print("Bestbuy Available")
            status_change()
        except NoSuchElementException:
            pass
        except TimeoutException:#common error thrown when website refuses to load
            print("TimeoutException")
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
        except StaleElementReferenceException:#common error thrown when website refuses to load
            print("StaleElementReferenceException")
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
        try:
            target_status = target.find_element_by_xpath("//button[@data-test='orderPickupButton']")
            print("Target Available")
            status_change()
        except NoSuchElementException:
            pass
        except TimeoutException:#common error thrown when website refuses to load
            print("TimeoutException")
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
        except StaleElementReferenceException:#common error thrown when website refuses to load
            print("StaleElementReferenceException")
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
        try:
            ms_status = ms.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/section/div/div/div/div/div/div[3]/button")
            ms_status = ms_status.text
            if ms_status != "Out of stock":
                print("Microsoft Available")
                status_change()
            else:
                pass
        except NoSuchElementException:
            pass
        except TimeoutException:#common error thrown when website refuses to load
            print("TimeoutException")
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
        except StaleElementReferenceException:#common error thrown when website refuses to load
            print("StaleElementReferenceException")
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
        time.sleep(8)
        bby.refresh()
        target.refresh()
        ms.refresh()

def status_change():
    print("*STATUS CHANGED*")
    speak("Status Changed")
    playsound('rick_roll.mp3')
    #plays 'never gonna give you up' when there is a change in a website

chrome_setup()