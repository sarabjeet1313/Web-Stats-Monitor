from bs4 import BeautifulSoup
import requests


URL = "https://www.worldometers.info/coronavirus/"

getSiteData = requests.get(URL).text
getPage = BeautifulSoup(getSiteData, "html.parser")
#print(getPage)


# Fetching global data

global_data = []

globalData = getPage.find_all("div" , {'class':'maincounter-number'})

for i in range(len(globalData)):
    value = [val.string for val in globalData[i].find_all("span")[0]]
    global_data.append(value[0])
