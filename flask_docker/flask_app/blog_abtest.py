from flask import Flask, jsonify, request, render_template, make_response, session
from db_model import mongodb
from db_model import mysql
from flask_login import LoginManager, current_user, login_user
from flask_cors import CORS
from blog_view import blog
from blog_control.user_mgmt import User
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

server = Flask(__name__, static_url_path='/static')
CORS(server)
server.secret_key = os.urandom(24)

server.register_blueprint(blog.blog_abtest)
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


#@login_manager.unauthorized_handler
#def unauthorized():
#    return make_response(jsonify(success=False), 401)

@server.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

@server.route('/')
def hello_blog():
    return 'Hello Blog'
