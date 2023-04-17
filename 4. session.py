from flask import Flask
from flask import request
from flask import render_template #載入render_template函式
from flask import session

app = Flask(__name__, static_folder= "public", static_url_path= "/www") 
app.secret_key = "any string but secret" #設定session的密鑰(必須動作)

@app.route("/")
def index():
    return render_template("index.html")

#使用GET方法處理路徑 /hello?name=使用者的名字
@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"] = name #session["欄位名稱"]=資料
    return "你好，"+ name


#使用GET方法處理路徑 /talk
@app.route("/talk")
def talk():
    name = session["username"]
    return name + ", 很高興見到你"

app.run(port = 3000)