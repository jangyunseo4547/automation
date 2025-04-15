from hdfs import InsecureClient
import os

client = InsecureClient('http://localhost:9870', user='ubuntu')

file_list = client.content('/input')

# localhost:9870에 cgv 폴더 생성 
client.makedirs('/input/cgv')

local_file_path = '/home/ubuntu/damf2/data/cgv/' 
hdfs_file_path = '/input/cgv/'

local_files = os.listdir(local_file_path)

for file_name in local_files:
    if not client.content(hdfs_file_path + file_name, strict=False):   # 해당 데이터가 있는지 체크
        client.upload(hdfs_file_path + file_name, local_file_path + file_name)
        # 없으면 업로드 