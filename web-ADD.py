# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:50:48 2020

@author: geraci
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


import requests
import urllib.request
import time

page = requests.get("http://www.paragear.com/parachutes/10000120/SKYDIVING-AAD")

print (page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

Parachute = soup.find(id="MainSection")

Manuf = []
mainParachute = []
StudParachute = []
tandemParachute = []
ReserveParachute = []

ManuCanopy = Parachute.find_all(class_="cattitles")
for i, ManuLink in enumerate(ManuCanopy):
    nameManuf = ManuLink.next_element
    print(nameManuf)
    ManufLink = ManuLink.get('href')
    canopysPage = requests.get(ManufLink)
#    print (nameManuf,page.status_code)
    soupCanopy = BeautifulSoup(canopysPage.content, 'html.parser')
    TopAreaCanopy = soupCanopy.find(id="MainSection")
    mainCanopy = TopAreaCanopy.find_all(class_="extCatTitleDark")
#    Manuf.append(nameManuf)

    for mainParaName in mainCanopy:
        Manuf.append(nameManuf)
        canopyLink = mainParaName.get('href')
#        print (canopyLink)
        parachutePage = requests.get(canopyLink)
#        print (page.status_code)
        soupMainCanopy = BeautifulSoup(parachutePage.content, 'html.parser')
        idCanopy = soupMainCanopy.find(id="ctl00_cpholder_ctl00_lDescription")
        CanopyName = idCanopy.next_element
        mainParachute.append(CanopyName.replace("HARNESS/CONTAINER","").replace("NO OPTIONS","").replace("-","").strip())
##
a = pd.DataFrame({"Manufacture":Manuf})
b = pd.DataFrame({"Container":mainParachute})
##c = pd.DataFrame({"Tandem Canopy":tandemParachute})
#####
Catalog = pd.concat([a, b], ignore_index=False, axis=1)
Catalog.to_csv('List-Manufacture&Add.csv', index=False)