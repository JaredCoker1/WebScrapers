# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:04:54 2021

@author: Jared Coker
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from playsound import playsound
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def chrome_setup():
    print("Setting up Chrome driver...")
    global options
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    global chrome_path
    chrome_path = os.path.expanduser("~/Desktop/chromedriver")
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
    init_status()

def init_status():
    global bby_status
    global target_status
    global ms_status
    bby_status = bby.find_element_by_class_name('add-to-cart-button')
    bby_status = bby_status.text
    print("Bestbuy status found as: " + bby_status)
    target_status = target.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]")
    target_status = target_status.text
    print("Target status found as: " + target_status)
    ms_status = ms.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/section/div/div/div/div/div/div[3]/button")
    ms_status = ms_status.text
    print("Microsoft status found as: " + ms_status)
    infinite_check(bby_status,target_status,ms_status)

def infinite_check(bby_status,target_status,ms_status):
    print("Now in infinite check...")
    i = 1
    #infinite loop that chacks to see if the status has changed of any of the 3 websites
    while bby_status == "Sold Out" and target_status == "Sold out" or target_status == "Out of stock in stores near you" and ms_status == "Out of stock":
        print("-------------------------------------------------")
        try:
            i+=1
            bby.refresh()
            target.refresh()
            ms.refresh()
            #refreshes page to check again
            bby_status = bby.find_element_by_class_name('add-to-cart-button')
            bby_status = bby_status.text
            target_status = target.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]")
            target_status = target_status.text
            ms_status = ms.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/section/div/div/div/div/div/div[3]/button")
            ms_status = ms_status.text
            print("New Bestbuy status found as: " + bby_status)
            print("New Target status found as: " + target_status)
            print("New Microsoft status found as: " + ms_status)
            #if there has been a change this if statement will break the loop
            if bby_status != "Sold Out" or target_status != "Sold out" or target_status != "Out of stock in stores near you" or ms_status != "Out of stock":
                if target_status == "Out of stock in stores near you":
                    pass
                else:
                    break
            print("Quick nap...")
            time.sleep(10)
            #sleeps for 2. minutes then loops through again
            print("This loop has ran "+str(i)+" times.")
        except NoSuchElementException:
            print("Could not find what you're looking for.")
            print("New Bestbuy status found as: " + bby_status)
            print("New Target status found as: " + target_status)
            print("New Microsoft status found as: " + ms_status)

        except TimeoutException:
            bby.close()
            target.close()
            ms.close()
            chrome_setup()
    status_change()

def status_change():
    print("*STATUS CHANGED*")
    print(str(time.perf_counter()))
    playsound('C:\\users\\jared\\onedrive\\documents\\STONKS\\rick_roll.mp3')
    #plays 'never gonna give you up' when there is a change in the website

chrome_setup()