from flask import request
from database import User
from database import UserModel
from database import config_db

db = config_db()

def Add_EditUser():
    user = request.json.get('user')
    models_id = request.json.get('models_id')
    # 没有该用户则添加
    if User.query.filter(User.id == user.get('pre_id')).first() is None:
        u = User()
        u.id = user.get('id')
        u.passwd = user.get('passwd')
        u.active = user.get('active')
        u.role = user.get('role')
        # 添加数据
        db.session.add(u)
        # 先添加用户数据，再添加用户模型数据
        db.session.commit()

        for model_id in models_id: # 遍历模型id列表
                um = UserModel(user_id=u.id, model_id=model_id) # 创建UserModel对象
                db.session.add(um) # 添加到数据库           
        # 提交会话 增删改都要提交会话
        db.session.commit()  
        
        return 'success'
    else:
        # 跟改了id
        if user.get('pre_id') != user.get('id'):
            User.query.filter(User.id == user.get('pre_id')).update({'id': user.get('id')})
            db.session.commit()
        # 跟改了passwd
        if user.get('pre_passwd') != user.get('passwd'):
            User.query.filter(User.id == user.get('id')).update({'passwd': user.get('passwd')})
            db.session.commit()
            
        # 实现增删模型权限，先删除所有该用户的所有UserModel，再添加记录
        # 查询所有user_id为user.get('id')的记录
        user_models = UserModel.query.filter(UserModel.user_id == user.get('id')).all()
        # 遍历结果集，逐个删除
        for user_model in user_models:
            db.session.delete(user_model)
        # 提交事务
        db.session.commit()
             
        for model_id in models_id: # 遍历模型id列表 
            db.session.add(UserModel(user_id=user.get('id'), model_id=model_id)) # 添加到数据库
        db.session.commit()

        return 'success'
    