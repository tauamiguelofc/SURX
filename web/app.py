from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client = MongoClient(os.getenv("MONGO_URI"))
db = client["surx_db"]
users = db["users"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = users.find_one({"username": request.form['username']})
        if user and user['password'] == request.form['password']:
            session['user'] = user['username']
            return redirect('/painel')
        return "Login inválido"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if users.find_one({"username": request.form['username']}):
            return "Usuário já existe"
        users.insert_one({
            "username": request.form['username'],
            "password": request.form['password']
        })
        return redirect('/login')
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'user' not in session:
        return redirect('/login')
    return render_template('painel.html', user=session['user'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
