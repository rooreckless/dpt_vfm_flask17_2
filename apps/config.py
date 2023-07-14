#from pathlib import Path
#basedir=Path(__file__).parent.parent
#各段階のconfigの基礎となる部分
class BaseConfig:
    SECRET_KEY="2AZSMss3p5QPbcY2hBsJ"
#開発段階のconfig(BaseConfigを継承)
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=f""
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO = True
    
#Test段階のconfig(BaseConfigを継承)
#Test段階ではCSRF対策を無効にするため「WTF_CSRF_ENABLED = False」
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=f""
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    WTF_CSRF_ENABLED = False

#辞書の中身は上のクラスを値にもつ キーが指定されたら、対応する設定値になる
config={"testing":TestingConfig,"local":LocalConfig}