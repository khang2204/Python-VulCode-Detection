from flask import Flask
from flask import redirect
from flask import url_for
from routes.topic_routes import topic_routes
from routes.auth_routes import auth_routes
from routes.reply_routes import reply_routes
app = Flask(__name__)
app.secret_key = 'for test'
@app.route('/', methods=['GET'])...
return redirect(url_for('auth.login'))
