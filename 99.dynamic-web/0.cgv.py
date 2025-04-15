from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
URL = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
driver.get(URL)
time.sleep(2)

movie_list= []

for i in range(3):
    # 무비 리스트를 매번 새로 불러오기 (stale 방지)
    movie_info = driver.find_elements(By.CSS_SELECTOR, 'div.box-contents > a')

    movie_info[i].click()
    time.sleep(2)  # 상세 페이지 로딩 대기

    title = driver.find_element(By.CSS_SELECTOR, 'div.title strong').text
    director = driver.find_element(By.CSS_SELECTOR, 'div.spec > dl > dd:nth-child(2)').text
    
    actor_list = []
    actors = driver.find_elements(By.CSS_SELECTOR, 'div.spec > dl > dd.on a')
    for actor in actors:
        actor.text
        actor_list.append(actor.text)
    
    
    genre = driver.find_element(By.CSS_SELECTOR, 'div.spec > dl > dt:nth-child(6)').text
    opening_date = driver.find_element(By.CSS_SELECTOR, 'div.spec > dl > dd:nth-child(11)').text

    movie_list.append([title, director, actor_list, genre, opening_date])

    driver.back()
    time.sleep(2)  # 다시 리스트 페이지 로딩 대기
    
local_file_path = '/home/ubuntu/damf2/data/cgv/'

def save_to_csv(movie_list):
    
    with open(local_file_path + 'cgv-movie.csv', mode= 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(movie_list)

save_to_csv(movie_list)