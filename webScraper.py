import requests
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup

def scraper():
    driver = webdriver.Chrome("/Users/stevenjiao/Documents/chromedriver")
    driver.get("https://www.placeprocanada.com/students/default.aspx")
    print(driver.title)
    driver.close()
    
    #driver.find_element_by_xpath("""//*[@id="txtLogin"]""").send_keys("StevenJiao")
    #driver.find_element_by_xpath("""//*[@id="txtPassword"]""").send_keys("StevenJiao1")
    #driver.find_element_by_xpath("""//*[@id="txtAccessCode"]""").send_keys("uofastu")
    #driver.find_element_by_xpath("""//*[@id="btnLogin"]""").click()
    #driver.get("https://www.placeprocanada.com/students/JobDetails.aspx?ID=55735&TID=3&YID=2020&CID=5098")

    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print(soup)

def login():
    
    scraper()


if __name__ == '__main__':
    scraper()

# Key: Company Name
# Array index order: Job title, Work level, Work duration, Location, Cover letter requirement