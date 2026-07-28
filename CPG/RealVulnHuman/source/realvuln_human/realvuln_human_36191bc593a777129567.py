from flask import Flask, request, render_template, redirect, make_response
import sqlite3

app = Flask(__name__)

# Hardcoded credentials (BAD PRACTICE)
USERNAME = "admin"
PASSWORD = "password123"

# Insecure database setup
def init_db():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    conn.commit()
    conn.close()
