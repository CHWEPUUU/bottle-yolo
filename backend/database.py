from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

def config_app():
    return app
def config_db():
    return db

class User(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    passwd = db.Column(db.String(16), nullable=False)
    active = db.Column(db.String(4), default=False)
    role = db.Column(db.String(8), nullable=False) 
    def __repr__(self):
        return '<User: %s %s >' % (self.id, self.passwd)
    
class Model(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    mAP50 = db.Column(db.Float, nullable=False)
    mAP95 = db.Column(db.Float, nullable=False)
    Recall = db.Column(db.Float, nullable=False)
    Params = db.Column(db.Integer, nullable=False)
    FLOPs = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return '<Model: %s >' % (self.id)   
    
class ImageData(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    img_name = db.Column(db.String(32), nullable=False)
    model = db.Column(db.ForeignKey(Model.id), nullable=False)
    img_size = db.Column(db.Integer, nullable=False)
    conf = db.Column(db.Float, nullable=False)
    iou = db.Column(db.Float, nullable=False)
    img_donwloadUrl = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return '<ImageData: %s >' % (self.id)   
    
class UserImageData(db.Model):
    user_id = db.Column(db.ForeignKey(User.id), primary_key=True)
    ImageData_id = db.Column(db.ForeignKey(ImageData.id), primary_key=True)
    def __repr__(self):
        return '<UserImageData: %s %s >' % (self.user_id, self.ImageData_id)
    
class UserModel(db.Model):
    user_id = db.Column(db.ForeignKey(User.id), primary_key=True)
    model_id = db.Column(db.ForeignKey(Model.id), primary_key=True)
    def __repr__(self):
        return '<UserModel: %s %s >' % (self.user_id, self.model_id)

with app.app_context():
    # 创建数据库
    db.create_all()
    