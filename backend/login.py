from flask import request
from database import User

def login():
    if request.method != 'POST':
        return

    username = request.json.get('username')
    passwd = request.json.get('password')
    guest = request.json.get('guest')

    if guest == 'guest':
        user = User.query.filter(User.id==guest).first()
        if user is not None and user.active == '是':
            return 'guest'
        else:
            return 'banned' 
    else:
        user = User.query.filter(User.id==username, User.passwd==passwd).first()
    
        if user is not None and user.active == '是':
            return 'successful/' + user.role
        elif user is not None and user.active == '否':
            return 'banned'
        else:
            return 'failed'
