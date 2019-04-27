import flask as fl
import database as db
import sys
import os

app = fl.Flask(__name__)
app.debug = True
@app.route('/')
def hello_world():
    fl.url_for("/")
    return app.send_static_file("index.html")

@app.route('/login',methods=['POST','GET'])
def login_page():
    if(fl.request.method=="POST"):
        login(fl.request.form['account'],fl.request.form['password'])


    return app.send_static_file("index.html")

def login(account,pwd):
    sql = 'SELECT pwd from users WHERE user="%s" ' %account
    print(sql)
    result = db.execute(sql)
    if(result[0]['pwd'] == pwd):
        return "sueec"
    else:
        return "fail"

if __name__ == '__main__':
    app.run()
