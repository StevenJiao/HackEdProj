import requests
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup



def scraper():
    driver = webdriver.Chrome("/Users/stevenjiao/Documents/placeProAuto/chromedriver")
    driver.get("https://ualberta.ca")
    contents = driver.page_source

    

def justforstorage():
    sportLinks = {
    "Badminton": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/badminton",
    "Basketball": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/basketball",
    "Dance Studio": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/dance-studio",
    "Foote Field": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/foote-field",
    "Group Fitness" :"https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/group-fitness",
    "Pickleball": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/pickle-ball",
    "Running": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/running",
    "Shinny": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/shinny",
    "Skating": "https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/skating",
    "Soccer":"https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/soccer",
   "Stick&Skate":"https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/stick-and-skate",
    "Swimming":"https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/swimming",
    "Tennis":"https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/tennis",
    "Volleyball":"https://www.ualberta.ca/kinesiology-sport-recreation/campus-community-recreation/drop-in/tennis"
    }
    
    for i in sportLinks:
        print(i)

    x = input()

    if (x in sportLinks):
        scraper(sportLinks[x])
        
    print("\n")


if __name__ == '__main__':
    scraper()



# Key: Company Name
# Array index order: Job title, Work level, Work duration, Location, Cover letter requirement