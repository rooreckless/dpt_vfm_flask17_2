from apps.config import config
from flask import Flask
from apps.testbp import views
from flask_cors import CORS
def create_app(config_key):
    app=Flask(__name__)
    app.register_blueprint(views.testbp,url_prefix="/testbp")
    app.config.from_object(config[config_key])
    #確認用にapp.configを出力してみます
    print("----app.config[SECRET_KEY]=",app.config['SECRET_KEY'])
    print("----app.config[SQLALCHEMY_ECHO]=",app.config['SQLALCHEMY_ECHO'])
    # CORS(app, resources={"/testbp/*":{"origins":"http://localhost:5173"}})
    CORS(app, resources={"/testbp/*":{"origins":"http://tmp/gunicorn_flask.sock"}})
    
    return app

if __name__=="__main__":
    app=create_app()
    # app.run()