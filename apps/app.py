from apps.config import config
from flask import Flask
from apps.testbp import views

def create_app(config_key):
    app=Flask(__name__)
    app.register_blueprint(views.testbp,url_prefix="/testbp")
    app.config.from_object(config[config_key])
    #確認用にapp.configを出力してみます
    print("----app.config[SECRET_KEY]=",app.config['SECRET_KEY'])
    print("----app.config[SQLALCHEMY_ECHO]=",app.config['SQLALCHEMY_ECHO'])
    return app

if __name__=="__main__":
    app=create_app()
    # app.run()