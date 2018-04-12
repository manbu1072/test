import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User - Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5 Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.162MobileSafari / 537.36'
}
urls = (
    'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E7%B4%A0%E6%8F%8F%E9%A3%8E%E6%99%AF')
wb_data = requests.get(urls, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('div > ul > li:nth-child(4) > div > a > img')
for
print(titles)
