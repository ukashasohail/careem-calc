from bs4 import BeautifulSoup
f = open("./data.txt", "r")
data = f.read()
soup = BeautifulSoup(data, "html.parser")
prices = []
raw = soup.find_all("div", class_="col-xs-5")

for i in raw:
    prices.append(float(i.string.strip()[3:].replace(',','')))

print("total price:", sum(prices))
print("total rides: ",len(prices))
print("avg price per ride: ", sum(prices)/len(prices))
