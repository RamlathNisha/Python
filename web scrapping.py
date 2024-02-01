from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver=webdriver.Chrome()
products=[]
prices=[]
orgprz=[]
off=[]
rating=[]
driver.get('https://www.flipkart.com/search?q=Laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&as-pos=1&as-type=HISTORY&as-backfill=on')
content=driver.page_source
soup=BeautifulSoup(content)
for a in soup.findAll(attrs={'class':'_1fQZEK'}):
    name=a.find('div',attrs={'class':'_4rR01T'})
    price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    orgprize=a.find('div',attrs={'class':'_3I9_wc _27UcVY'})
    offer=a.find('div',attrs={'class':'_3Ay6Sb'}).find('span')
    rat=a.find('div',attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    orgprz.append(orgprize.text)
    off.append(offer.text)
    rating.append(rat.text)
df=pd.DataFrame({'Product Name':products,'Selling Price':prices,'Original Price':orgprz,'Offer Percentage':off,'Ratings out of 5':rating})
df.to_csv('products.csv',index=False,encoding='utf-8')