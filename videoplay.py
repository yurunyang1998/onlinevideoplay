import flask as fl

app = fl.Flask(__name__)


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
    pass
    
if __name__ == '__main__':
    app.run()
