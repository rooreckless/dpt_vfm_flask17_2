chdir = "/home/ec2-user/dpt_vfm_flask17_2/apps"
wsgi_app = "apps.app:create_app('local')"
workers = 2
# /tmp ディレクトリにソケットができる
socket_path = 'unix:/tmp/gunicorn_flask.sock'
bind = socket_path
#開発時はreload=True
reload = True