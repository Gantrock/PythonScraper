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

print(soup.prettify())
