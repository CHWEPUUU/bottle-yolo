import pprint
import requests
from io import BytesIO
from flask import request
from uploadImg import upload
import numpy as np
import cv2
import os
import time
from database import ImageData
from database import UserImageData
from database import config_db

db = config_db()

def detect():
    username = request.json.get('username')
    model = request.json.get('model')
    img_size = request.json.get('img_size')
    conf = request.json.get('conf') / 100
    iou = request.json.get('iou') / 100
    img = request.json.get('img')
    fileName = request.json.get('fileName')
    DETECTION_URL = f'http://localhost:8081/{model}/{img_size}/{conf}/{iou}'
    IMAGE_URL = img

    # print(DETECTION_URL)
    response = requests.get(IMAGE_URL, stream=True)
    # Read image
    # f = BytesIO(response.content)
    # image_data = f.read()
    image_data = response.content

    # print(image_data)

    # response = requests.post(DETECTION_URL, files={'image': image_data}).json()
    response = requests.post(DETECTION_URL, files={'image': image_data})
    # 保存为图片
    img = cv2.imdecode(np.frombuffer(response.content, dtype=np.uint8), cv2.IMREAD_COLOR)
    result_img = f'{model}-{img_size}-{conf}-{iou}-{fileName}'
    
    cv2.imwrite(result_img, img)   
    img_url = upload(result_img)
    os.remove(result_img)
    
    # 添加imageData数据
    imageData = ImageData()
    imageData.id = time.time()
    imageData.img_name = fileName.split('.')[0]
    imageData.model = model
    imageData.img_size = img_size
    imageData.conf = conf
    imageData.iou = iou
    imageData.img_donwloadUrl = img_url
    # 添加UserImageData数据
    userImageData = UserImageData()
    userImageData.user_id = username
    userImageData.ImageData_id = imageData.id

    with db.session.begin():  
        db.session.add(imageData)
        db.session.add(userImageData)
    # 提交会话 增删改都要提交会话
    db.session.commit()  
    
    # pprint.pprint(response)
    return img_url