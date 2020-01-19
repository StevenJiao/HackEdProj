import requests
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup

def scraper():
    page = requests.get("https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/badminton")
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.prettify())



if __name__ == '__main__':
    scraper()

# Key: Company Name
# Array index order: Job title, Work level, Work duration, Location, Cover letter requirement