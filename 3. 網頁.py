from flask import Flask
from flask import request
from flask import render_template #載入render_template函式

app = Flask(__name__, static_folder= "public", static_url_path= "/www") 

#使用GET方法，處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page")
def page():
    return render_template("page.html")

#使用POST方法，處理路徑 /calculate 的對應函式
@app.route("/calculate", methods = ["POST"]) 
def calculate():
    #接收 GET 方法的 Query String
    # maxNumber = request.args.get("max","")

    #接收 POST 方法的 Query String
    maxNumber = request.form["max"]
    maxNumber = int(maxNumber)
    result = 0
    for n in range (1,maxNumber+1):
        result += n
    return render_template("result.html", data = result)

@app.route("/show")
def show():
    name = request.args.get("n","")
    return "歡迎光臨, "+name


app.run(port = 3000)