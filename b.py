import requests
from bs4 import BeautifulSoup
import time
headers = {
    'User - Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5 Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.162MobileSafari / 537.36'
}
f = open('F:/1.txt','a+')
urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1)]
for url in urls:
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select("span.pc_temp_tips_r > span")
    for rank,title,time in zip (ranks,titles,times):
        data = {
            '排名': rank.get_text().strip(),
            '歌手': title.get_text().split('-')[0],
            '歌名': title.get_text().split('-')[1],
            '时间': time.get_text().strip()
        }
        datas = str(data)
        f.write(datas+'\n')
f.close()