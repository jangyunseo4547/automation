from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()

URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)


song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')
# print(len(song_info))

song_list = []

for i in range(3):
    song_info[i].click()
    time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text # element 안에 있는 텍스트 값만 출력
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist > a > span').text  # 꺽쇠 : 직계 / 공란 : 후손 의미
    
    #1) 전체 dd를 가져오고, 인덱스에 접근한 경우  
    meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd')
    print(meta_data[1].text)

    #2) 발매일 정보를 특정
    publish_date = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    like_cnt = like_cnt.replace(',', '') # 쉼표를 대체함
 
    song_list.append([title,])

    driver.back()

local_file_path = '/home/ubuntu/damf2/data/melon/'

def save_to_csv(song_list):
    
    with open(local_file_path + 'melon-top-100.csv', mode= 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(song_list)

save_to_csv(song_list)