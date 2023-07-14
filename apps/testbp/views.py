from flask import Flask,Blueprint,render_template,redirect,flash,url_for,request
#ブループリントを作成
# url_prefixを追加したBlueprintオブジェクトを作成
testbp = Blueprint("testbp",__name__,url_prefix="/testbp",template_folder='templates',static_folder='static')

#auth側のルーティングを記載
@testbp.route("/")
def index():
    #apps/testbp/templates の中の、testbp/index.htmlを指定
    return render_template("testbp/index.html")