from datetime import datetime
import requests
import time
import csv

upbit_url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'

start_time = time.time()
# print(start_time)


bit_data_list = []

while time.time() - start_time < 60: 
    res = requests.get(upbit_url)
    data = res.json()[0]

    bit_data = [
        data['market'],
        data['trade_date'],
        data['trade_time'],
        data['trade_price']
    ]
    bit_data_list.append(bit_data)
    time.sleep(5) # 5초에 한번씩 요청을 보내고 1분이 지나면 요청 중단

    print(bit_data_list)

local_file_path = '/home/ubuntu/damf2/data/bitcoin/'

now = datetime.now()
file_name = now.strftime('%H-%M-%S') + '.csv' # strftime:데이터 타입 객체를 글자로 바꿈.

with open(local_file_path + file_name, mode='w', newline='') as file: # open : 특정 os 경로에 있는 파일을 열어줌. -> with문이 실행이 되는 한 파일이 열림/ 이를 file이라는 변수에 저장
    writer = csv.writer(file)
    writer.writerows(bit_data_list)
