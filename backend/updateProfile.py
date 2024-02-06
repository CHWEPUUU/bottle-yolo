from flask import request
from database import User
from database import config_db

db = config_db()

def updateProfile():
    if request.method != 'POST':
        return

    username = request.json.get('username')
    change_username = request.json.get('change_username')
    passwd = request.json.get('passwd')

    if(username == change_username):
        User.query.filter(User.id == username).update({'passwd': passwd})
        db.session.commit()
    else:
        User.query.filter(User.id == username).update({'id': change_username, 'passwd': passwd})
        db.session.commit()
    
    return "successfully updated personal profile"
