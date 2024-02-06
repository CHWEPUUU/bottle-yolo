import os 
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
from flask import request
from io import BytesIO

APP_ID = 'ddaa8b00-7a73-4cdf-813c-fe042130fb9e'
SCOPES = ['Files.ReadWrite']
access_token = generate_access_token(APP_ID, SCOPES)

headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = r'c:\Users\CHWEPUUU\Pictures\A0708A3D855569503CB87564E3EC035F.jpg'
file_name = os.path.basename(file_path)

with open(file_path, 'rb') as upload:
   media_content = upload.read()
   
# 上传文件
# reponse = requests.put(
#     GRAPH_API_ENDPOINT + f'/me/drive/items/root:/yolo_img/{file_name}:/content',
#     headers=headers,
#     data=media_content
# )
# print(reponse.json())

# 获取文件
save_location = os.getcwd()
reponse = requests.get(
    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/yolo_img/A0708A3D855569503CB87564E3EC035F.jpg',
    headers=headers
)

# print(reponse.json().get('webUrl'))
print(reponse.json())

