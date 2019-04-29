import flask as fl
import database as db
import sys
import os

app = fl.Flask(__name__)
app.debug = True
@app.route('/')
def hello_world():
    return app.send_static_file("index.html")

@app.route('/login',methods=['POST','GET'])
def login_page():
    if(fl.request.method=="POST"):
        owner = fl.request.form['account']
        result = login(fl.request.form['account'],fl.request.form['password'])
        if(result==0):
            return fl.redirect(fl.url_for("movies",owner=owner))
    else:
        return app.send_static_file("index.html")


def login(account,pwd):
    sql = 'SELECT pwd from users WHERE user="%s" ' %account
    print(sql)
    result = db.execute(sql)
    if(result[0]['pwd'] == pwd):
        return 0;
    else:
        return -1

@app.route("/movies/<owner>",methods=["POST","GET"])
def movies(owner):
    owner = str(owner)
    sql = 'SELECT movie from movies WHERE owner="$s" ' %owner
    result = db.execute(sql)
    print(result)
    return fl.render_template("chosevideos.html")


if __name__ == '__main__':
    app.run()
