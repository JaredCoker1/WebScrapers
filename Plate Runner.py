# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:39:37 2021

@author: jared
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from playsound import playsound
import time

def user_info():
    global plate
    global state
    plate = input("Plate number: ")
    state = input("State: ")

def driver_setup():
    global options
    options = Options()
    options.add_argument("--disable-gpu")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument('--profile-directory=Profile 1')
    chrome_path = r"C:\Users\jared\desktop\chromedriver.exe"
    tab = webdriver.Chrome(executable_path = chrome_path, options = options)
    insert_page = "https://www.vehiclehistory.com/license-plate-search"
    tab.get(insert_page)
    plate_num_input =  WebDriverWait(tab, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[4]/div/div[1]/div[2]/div/div/div/form/div[1]/div/div[1]/div[1]/input")))
    plate_num_input.send_keys(plate)
    plate_state1 = tab.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/form/div[2]/div/div[1]/div[1]')
    plate_state1.click()
    plate_state2 = tab.find_element_by_class_name("VhMenu-menuContent")
    #tab.execute_script("document.getElementsByClassName('VhMenu-menuCont\ent').style = 'max-height:2600px;'")
    tab.execute_script("arguments[0].setAttribute('style','height:2600px')", plate_state2)
    #tab.execute_script("window.scrollTo(0, 2600)") 
    #plate_state3 = tab.find_element_by_id("list-2-"+str(state))
    #plate_state3.click()     
    #search_btn = tab.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div/div[1]/div[2]/div/div/div/form/div[3]/button')
    #search_btn.click()
    
user_info()
driver_setup()