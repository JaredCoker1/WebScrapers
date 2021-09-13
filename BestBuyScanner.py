# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:05:08 2021

@author: jared
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from playsound import playsound
import time
from twilio.rest import Client
import os

# =============================================================================
# from win32com.client import Dispatch
# 
# speak = Dispatch("SAPI.SpVoice").Speak
# 
# speak("Wake the fuck up and check the computer, you have an xbox available!")
# =============================================================================

def twilio_setup():
     account_num = '***********************'
     token =  '********************'
     global client
     client = Client(account_num, token)

def driver_setup():
    global options
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument('--user-data-dir=C:\\Users\\jared\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument('--profile-directory=Profile 1')
    chrome_path = r"C:\Users\jared\documents\STONKS\chromedriver.exe"
    global bby
    bby = webdriver.Chrome(executable_path = chrome_path, options = options)
    bby_url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
    bby.get(bby_url)
    global delay
    delay = 5
    global bby_status
    #time.sleep(1)
    bby_status = bby.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button')
    bby_status = bby_status.text
    print("Status is: "+str(bby_status))
    #client.messages.create(from_='+13392290897', body = '\n\nScan started.\n', to = '+15126602545')
    inf_check(bby_status)
    
def inf_check(bby_status):
    i = 0
    while bby_status == "Sold Out":
        i+=1
        try:
            bby.refresh()
            print("Page refreshed")
            time.sleep(6)
            bby_status = bby.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button')
            bby_status = bby_status.text
            print("Status is: "+str(bby_status))
            if i%100 == 0:
                print("Sucessful runs: "+str(i))
            print("Quick nap...")
            #time.sleep(3)
        except TimeoutException as ex:
            playsound('C:\\Users\\jared\\documents\\STONKS\\ding.mp3')
            print("Error occured in inf check: "+str(ex))
            
        except NoSuchElementException:
            print("Bestbuy tried to stop you...\nRestarting Browser...")
            bby.close()
            driver_setup()
    bby_status = bby.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button')
    add_to_cart(bby_status)

def add_to_cart(bby_status):
    bby_status = bby_status.text
    while bby_status != "Sold Out":
        try:
            bby_status = bby.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button')
            bby_status.click()
            #time.sleep(1)
            go_to_cart()
            
        except TimeoutException as ex:
            playsound('C:\\Users\\jared\\documents\\STONKS\\ding.mp3')
            print("Error occured when adding to cart: "+str(ex))
            add_to_cart(bby_status)
            
def go_to_cart():
    print("Item has sucessfully been added to cart.")
    try:
        go_to_cart_btn = WebDriverWait(bby, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a')))
        #time.sleep(1)
        go_to_cart_btn.click() 
        #time.sleep(1)
        Checkout()
        
    except TimeoutException as ex:
        playsound('C:\\Users\\jared\\documents\\STONKS\\ding.mp3')
        print("Error occured when going to cart: "+str(ex))
        go_to_cart()
      
def Checkout():
    print("Sucessfully navigated to your cart.")
    try:
        checkout = WebDriverWait(bby, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')))
        checkout.click()
        check_if_done()
    except TimeoutException as ex:
        playsound('C:\\Users\\jared\\documents\\STONKS\\ding.mp3')
        print("Error occured when checking out: "+str(ex))
        Checkout()

def check_if_done():
    try:
        time.sleep(2)
        bby.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/section[1]/div[2]/section/div/div[5]/div[2]/span')
    except NoSuchElementException:
        print("So close to checkout...")
        playsound('C:\\Users\\jared\\documents\\STONKS\\ding.mp3')
        Checkout()
    print("You have been checked out sucessfully!")
    #client.messages.create(from_='+13392290897', body = '\n\nYou have sucessfully acquired an xbox!\n', to = '+15126602545')
    playsound('C:\\Users\\jared\\documents\\STONKS\\rick_roll.mp3')

#twilio_setup()
driver_setup()