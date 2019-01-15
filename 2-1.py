'''
날짜 : 19-01-14
내용 : 파이선 파싱연습
'''
from bs4 import BeautifulSoup as bs
import urllib.request as req

url = "http://chhak.com/py/test1.html"
html = req.urlopen(url)

dom = bs(html, 'html.parser')
title = dom.select_one('h1').string
items = dom.select('li')

print('제목 : ', title)

for li in items:

    print('아이템 : ', li.string)