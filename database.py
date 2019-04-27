import  sqlite3

import flask as fl
import os,sys

path = sys.path[0]
DATABASE = path+"\\DATABASE"
DATABASE_INIT_FILE = path+"\\init.sql"
app = fl.Flask("post")


def init_db():
    with app.app_context():
        db = get_db()
        with   app.open_resource(DATABASE_INIT_FILE,'r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        print("create database ")


def make_dicts(cursor, row):  # 将查询返回的数据的转换为字典类型，这样会跟方便使用。此函数会在get_db()函数中用到，赋值给db.row_factory。
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_db():  # 获取数据库连接
    db = getattr(fl.g, '_database', None)  # g对象时一个Flask应用的公共对象（和request、session一样），用于存储用户的数据——整个应用共享！
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)  # 建立数据库连接
        db.row_factory = make_dicts  # 转换默认的查询数据类型为字典类型，也可以使用sqlite3.Row
    return db  # 返回数据库连接，可能返回为None



@app.route('/test')
def db():
    db = get_db()
    if (db):
        return "hahahahaha"

def execute(sql):
    with app.app_context():
        try:
            db=  get_db()
            cursor =db.execute(sql)
            db.commit()
            rv = cursor.fetchall()
            cursor.close()
            if(rv):
                return rv
        except Exception as e:
            print(e)
            return 500



if __name__ == '__main__':

    execute('SELECT users.pwd from users WHERE users.user=admin;')