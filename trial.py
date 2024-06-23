import requests
from bs4 import BeautifulSoup

def extract(page):
  headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

  url = f"https://ca.indeed.com/jobs?q=python+developer&l=Montreal&start={page}"

  r = requests.get(url,headers)
  return r.status_code

print(extract(0))

