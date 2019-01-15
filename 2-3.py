'''
날짜 : 19-01-15
내용 : 부산일보 로그인하기
'''

import requests as req
from bs4 import BeautifulSoup as bs

#세션 시작
sess = req.session()

#로그인하기
id = 'ksb0503'
pw = '123456789'
login_Check_rul = 'https://here.busan.com/bbs/login_check.php'
sess.post(login_Check_rul, data={'mb_id': id, 'mb_password': pw})

#마이페이지
my_page_url = 'https://here.busan.com/member/member_mypage.php'
res = sess.get(my_page_url)
#독자투고 페이지 이동

#나의 정보 스크래핑하기
dom = bs(res.text, 'html.parser')
id = dom.select_one('#design_contents > dl > dd > span.id')
point = dom.select_one('#design_contents > div.point > font:nth-of-type(1)')

print("아이디 : ", id.string)
print("포인트 : ", point.string)
