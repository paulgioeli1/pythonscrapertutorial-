#First Python Scraper

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = "ResultsContainer")
#print(results.prettify())

job_elements = soup.find_all("div", class_ = "card-content" )
#print(job_elements)

for job in job_elements:
    print(job, end = "\n"*2)
