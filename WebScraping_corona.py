import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

r = requests.get(url)
#print(r)
s = BeautifulSoup(r.content, "html.parser")
#print(s)

data = s.find_all("div", class_ = "maincounter-number")
#print(data)
head = s.find_all("h1")

print(head[0].get_text().strip() +" "+ data[0].get_text().strip())
print(head[1].get_text().strip()+ " " +data[1].get_text().strip())
print(head[0].get_text().strip()+ " "+data[2].get_text().strip())
