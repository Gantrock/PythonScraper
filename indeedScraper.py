import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

#The url
URL = "https://www.indeed.com/jobs?q=software+developer&l=Washington+State&ts=1523564253543&rq=1&fromage=last"

#performing the get request on the URL
page = requests.get(URL);

#Specifying the format for the parser
soup = BeautifulSoup(page.text, "html.parser")

#Extracts job titles from the html
def extract_job_title_from_result(soup):
  jobs = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
      for a in div.find_all(name="a", attrs= {"data-tn-element":"jobTitle"}):
        jobs.append(a["title"])
  return(jobs)
      
#print(soup.prettify())
extract_job_title_from_result(soup)
