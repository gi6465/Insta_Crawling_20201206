#20201206-08:48 PM

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


SrchMd = int(input('1.ID 2.Search Hashtag : '))
while SrchMd != 1 and SrchMd != 2:
    print('! Wrong Value')
    SrchMd = int(input('1.ID 2.Search Hashtag : '))

baseUrl = 'https://www.instagram.com'
if SrchMd == 1:
    InputValue = quote_plus(input('Enter ID : '))
    PlusUrl = '/' + InputValue
else:
    InputValue = quote_plus(input('Enter Hashtag'))
    PlusUrl = '/explore/tags/' + InputValue

url = baseUrl + PlusUrl

createFolder('./img/' + InputValue)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

insta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1
for i in insta:
    print(baseUrl + i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + InputValue + PlusUrl + str(n) + '.jpg', "wb") as h:
            img = f.read()
            h.write(img)
    n += 1

driver.close()





