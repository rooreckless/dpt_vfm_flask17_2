from flask import Flask,Blueprint,jsonify
import datetime
#ブループリントを作成
# url_prefixを追加したBlueprintオブジェクトを作成
testbp = Blueprint("testbp",__name__,url_prefix="/testbp",template_folder='templates',static_folder='static')

#以下はflaskで描画するためのルートなので潰します
# @testbp.route("/")
# def index():
#     return render_template("testbp/index.html")

#vueからのアクセステスト用のルートです
@testbp.route("/testroute",methods=["GET"],endpoint="testfectchapi")
def testfectchapi():
  dt_now = datetime.datetime.now()
  return jsonify({"flask-- @testbp.route(/testroute)":"is finished",
                  "nowtime":dt_now.strftime('%Y年%m月%d日 %H:%M:%S')})