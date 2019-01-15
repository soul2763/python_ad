'''
날짜 : 19-01-14
내용 : 네이버 뉴스 파싱연습
'''

from bs4 import BeautifulSoup as bs
import urllib.request as req

url = "https://news.naver.com/"
html = req.urlopen(url)

dom = bs(html, 'html.parser')
title = dom.select_one('h4').string
strong = dom.select('#text_today_main_news_801001 > li > div > a > strong')

title1 = dom.select_one('#section_economy > div.com_header > h4 > a').string
strong1 = dom.select('#section_economy > div.com_list > div > ul > li > a > strong')

print('제목 : ', title)

for li in strong:

    print('title : ', li.text)


print('제목 : ', title1)

for li in strong1:

    print('title : ', li.text)