import subprocess
import requests
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: Insecure Use of Subprocess (Command Injection)
@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', '')
    result = subprocess.check_output(['ping', '-c', '4', ip])
    return result

# Vulnerability 2: Hardcoded Credentials
USERNAME = 'admin'
PASSWORD = 'password123'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
