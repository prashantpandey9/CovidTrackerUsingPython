"""This script is used to track the total case in india."""
import requests
from bs4 import BeautifulSoup
import time
url="https://www.mygov.in/covid-19"
q=requests.get(url)
r=BeautifulSoup(q.text,"html.parser")
data=r.find_all("span",class_="icount")

print("ACTIVE CASES:",data[0].text.strip())
print("CURED/DISCHARGED CASES:",data[1].text.strip())
print("DEATHS CASES:",data[2].text.strip())
print("MIGRATED CASES:",data[3].text.strip())
print("time",time.ctime())
