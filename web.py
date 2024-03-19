import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

resp = requests.get(url)

if resp.status_code == 200:
    print("Success")
    soup = BeautifulSoup(resp.text, 'html.parser')
    l = soup.find()
    print(l.text)
else:
    print("Error")
