from flask import Flask,Blueprint,render_template,redirect,flash,url_for,request,jsonify
#ブループリントを作成
# url_prefixを追加したBlueprintオブジェクトを作成
testbp = Blueprint("testbp",__name__,url_prefix="/testbp",template_folder='templates',static_folder='static')

# @testbp.route("/")
# def index():
#     return render_template("testbp/index.html")
#テスト用のルーティングです
@testbp.route("/testroute",methods=["GET"],endpoint="testfectchapi")
def testfectchapi():
  return jsonify({"flask-- @back_app.route(/test":"is finished"})