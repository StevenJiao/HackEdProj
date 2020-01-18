import requests
from lxml import html
from bs4 import BeautifulSoup

page = requests.get("https://www.placeprocanada.com/students/JobDetails.aspx?ID=55735&TID=3&YID=2020&CID=5098")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

def login():
    session_requests = requests.session()
    login_url = "https://www.placeprocanada.com/students/JobDetails.aspx?ID=55735&TID=3&YID=2020&CID=5098"
    login_result = session_requests.get(login_url)

