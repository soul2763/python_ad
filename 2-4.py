'''
날짜 : 19-01-15
내용 : 가상 웹브라우저 실행하기
'''

#크롬 드라이버 실행
from selenium import webdriver
browser = webdriver.Chrome('./chromedriver.exe')

#네이버 이동
browser.get('http://www.naver.com')

#네이버 로그인 버튼 클릭
login_btn = browser.find_element_by_css_selector('#account > div > a')
login_btn.click()

#아이디, 비밀번호 입력
input_id = browser.find_element_by_id('id')
input_pw = browser.find_element_by_id('pw')

input_id.send_keys('abcdaf')
input_pw.send_keys('asdfsf')

#로그인버튼 클릭
login_btn2 = browser.find_element_by_css_selector('#frmNIDLogin > fieldset > input')
login_btn2.click()