from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from login import login
from database import config_app
from database import config_db
from uploadImg import upload
from detectImg import detect
from updateProfile import updateProfile
from add_edit import Add_EditUser
from database import User, ImageData, UserImageData, Model, UserModel
import json
from PIL import Image
import argparse
import io
import torch
import cv2

app = config_app()
db = config_db()
models = {} # 有哪些模型

# 模型文件路径和权重路径
path = {'yolov7-gold':'21_yolov7_gold', 'yolov7':'0_yolov7_tiny', 'yolov7-ICCV':'24_yolov7_ICCV'}
weight = {'yolov7-gold':'yolov7-tiny-gold.pt', 'yolov7':'yolov7-tiny.pt', 'yolov7-ICCV':'yolov7-tiny-ICCV.pt'}
# 权重基本路径
base_path = 'F:\Code\Code_Vue\yolo\yolov7\yolov7.pt'

DETECTION_URL = '/<model>/<image_size>/<confidence_threshold>/<iou_threshold>'

@app.route('/login', methods=['POST'])
def Login():
    return login()

@app.route('/upload', methods=['POST'])
def Upload():
    return upload('')

@app.route('/detect', methods=['POST'])
def Detect():
    return detect()

@app.route('/updateProfile', methods=['POST'])
def UpdateProfile():
    return updateProfile()

@app.route('/users', methods=['GET'])
def GetUsers():
    users = User.query.all()
    return json.dumps([{"id": user.id, "active": user.active, "role": user.role, "passwd": user.passwd} for user in users])

@app.route('/models', methods=['GET'])
def GetModels():
    models = Model.query.all()
    return json.dumps([{"model": model.id, "mAP50": model.mAP50, "mAP95": model.mAP95, "Recall": model.Recall, "Params": model.Params, "FLOPs": model.FLOPs} for model in models])

@app.route('/userModels', methods=['post'])
def GetUserModels():
    user_id = request.json.get('username')
    models = UserModel.query.filter(UserModel.user_id == user_id).all()
    return json.dumps([{"value": model.model_id, "label": model.model_id} for model in models])


@app.route('/deleteUser', methods=['POST'])
def DeleteUsers():
    id = request.json.get('id')
    # 删除数据
    db.session.delete(User.query.filter(User.id == id).first())
    # 提交会话 增删改都要提交会话
    
    # 查询所有user_id为user.get('id')的记录
    user_models = UserModel.query.filter(UserModel.user_id == id).all()
    # 遍历结果集，逐个删除
    for user_model in user_models:
        db.session.delete(user_model)
    # 提交事务
    db.session.commit()
    return "index"

@app.route('/addEditUser', methods=['POST'])
def AddEditUser():
    return Add_EditUser()

@app.route('/addUserModel', methods=['POST'])
def AddUserModel():
    user_id = request.json.get('user_id')
    models_id = request.json.get('models_id')
    
    for model_id in models_id: # 遍历模型id列表
        um = UserModel(user_id=user_id, model_id=model_id) # 创建UserModel对象
        db.session.add(um) # 添加到数据库

    # 提交会话 增删改都要提交会话
    db.session.commit()  
    return "index"

@app.route('/updateActive', methods=['POST'])
def UpdateActive():
    id = request.json.get('id')
    active = request.json.get('active')
    # 更新数据
    User.query.filter(User.id == id).update({'active': active})
    # 提交会话 增删改都要提交会话
    db.session.commit()  
    return "index"

@app.route('/ImageData', methods=['POST'])
def GetImageData():
    user_id = request.json.get('username')
    imageDatas = db.session.query(User, UserImageData, ImageData).join(UserImageData, User.id == UserImageData.user_id).join(ImageData, UserImageData.ImageData_id == ImageData.id).filter(User.id == user_id).all()
    return json.dumps([{"id": imageData.id, "img_name": imageData.img_name, "model": imageData.model, 
                        "img_size": imageData.img_size, "conf": imageData.conf, "iou": imageData.iou,
                        "img_donwloadUrl": imageData.img_donwloadUrl} for _, _, imageData in imageDatas])
    
@app.route('/deleteImage', methods=['POST'])
def DeleteImageData():
    id = request.json.get('id')
    # 删除数据
    db.session.delete(ImageData.query.filter(ImageData.id == id).first())
    # 提交会话 增删改都要提交会话
    db.session.commit()
    return "index"

@app.route(DETECTION_URL, methods=['POST'])
def predict(model, image_size, confidence_threshold, iou_threshold):
    if request.method != 'POST':
        return

    if request.files.get('image'):
        # Method 1
        # with request.files["image"] as f:
        #     im = Image.open(io.BytesIO(f.read()))

        # Method 2
        im_file = request.files['image']
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))

        if model in models:
            models[model].conf = float(confidence_threshold)
            models[model].iou = float(iou_threshold)
            results = models[model](im, size=int(image_size))  # reduce size=320 for faster inference
            results = results.render()[0]
            return cv2.imencode('.jpg', results)[1].tobytes()
            # return results.pandas().xyxy[0].to_json(orient='records')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Flask API exposing YOLOv7 model')
    parser.add_argument('--model', nargs='+', default=['yolov7-gold', 'yolov7'], help='model(s) to run, i.e. --model yolov5n yolov5s')
    opt = parser.parse_args()
    
    # 加载模型
    # for m in opt.model:
    models['yolov7'] = torch.hub.load('F:\Code\Code_Vue\yolo\yolov7', "custom", path_or_model=base_path, source="local")
    models['yolov7-tiny'] = torch.hub.load('F:\Code\Code_Vue\yolo\yolov7', "custom", path_or_model='F:\Code\Code_Vue\yolo\yolov7\yolov7-tiny.pt', source="local")

    app.run(debug=True, port=8081)