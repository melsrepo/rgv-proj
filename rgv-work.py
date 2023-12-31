import pandas as pd
from bs4 import BeautifulSoup
import requests

#define function to scrape and store the data
def getData(url):
    response = requests.get(url)
    respTxt = BeautifulSoup(response.text,
                            "lxml") #converting the html to text

    #gets all the organizarion names
    orgs = respTxt.find_all("h3", attrs={"aria-expanded": "true"})


    #gets the org info
    info = respTxt.find_all("p")

    #all the orgs are now in one list
    orgList = []
    for elements in orgs:
        orgList.append(elements.text)

    # all the orgs' info is now in one list
    infoList = []
    #does not have a new line character
    for elements in info:
        infoList.append(elements.text)
    #combine the lists into a dictionary
    orgInfoList = dict(zip(orgList, infoList))

    return orgInfoList

    #they are not the same length
    # print(len(orgList))
    # print(len(infoList))
    #we need to split infoList into five lists one for each br. We want 6 columns
def exportDate(data):
    df = pd.DataFrame(data = data, index = [0])
    df.to_excel("rgv-sheet.xlsx")
d = getData("https://rgvpartnership.com/rgv-non-profit-organizations/?fbclid=IwAR1pt2PXiA7R94dHuUgvsWGURo7eLTKDySVz6t5dS_6xb1fFn1MH2jAnDkQ")
exportDate(d)


