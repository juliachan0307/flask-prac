from flask import Flask
from flask import request
from flask import redirect #載入redirect函式
import json

#建立Application的物件,可以設定靜態檔案路徑處理
app = Flask(
    __name__,
    static_folder= "public", #靜態檔案的資料夾名稱,預設是static
    static_url_path= "/www" #靜態檔案對應的網址路徑,預設是/static
#所有再public資料夾底下的檔案，都對應到網址路徑 /檔案名稱
    )  

#建立路徑 /getSum 對應的處理函式
#利用要求字串 (Query String) 提供彈性 /getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum(): #min+(min+1)++(min+2)...+max
    maxNumber = request.args.get("max", 100)
    maxNumber = int(maxNumber)
    minNumber = request.args.get("min", 1)
    minNumber = int(minNumber)
    result = 0
    for n in range (minNumber,maxNumber+1):
        result += n
    return "結果:" + str(result)

#建立路徑 /en/, /zh-tw/ 對應的處理函式
@app.route("/en/")
def index_english(): 
    return json.dumps({
            "status": "ok",
            "text": "Hello World"
        })
@app.route("/zh-tw/")
def index_chinese(): 
    return json.dumps({
            "status": "ok",
            "text": "您好 世界"
    }, ensure_ascii=False) #指示不要用ASCII編碼處理中文



#使用GET方法，處理路徑 / 的對應函式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    #----------------------------------------------------------------------
    lang = request.headers.get("accept-language") #語言偏好
    if lang.startswith("en"):
        return redirect("/en/") #導向到路徑/en/
    else:
        return redirect("/zh-tw/") #導向到路徑/en/
    
#建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData(): 
    return "My Data"

#建立動態路由:建立路徑 /user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleuser(username): 
    return "Hello " + username

#啟動網站伺服器，可透過Port參數指定埠號
app.run(port = 3000)