from flask import Flask
from flask import request
from flask import render_template #載入render_template函式

app = Flask(__name__, static_folder= "public", static_url_path= "/www") 


@app.route("/")
def index():
    return render_template("index", name = "JC")

app.run(port = 3000)