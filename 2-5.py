'''
날짜 : 19-01-15
내용 : 네이버 실검 크롤링
'''


import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

res = req.get('http://naver.com')
dom = bs(res.text, 'html.parser')

titles = dom.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

#for li in titles:
#    print(li.text)

#파일생성
fname = "{:%y-%m-%d-%h-%M.txt}".format(datetime.now())
file = open(fname, mode='w',encoding='utf-8')

#파일쓰기
for tit in titles:
    file.write(tit.text+'\n')

file.close()
