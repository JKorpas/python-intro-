import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
html = response.text

soup = BeautifulSoup(html, "html.parser")
title = soup.title.text
