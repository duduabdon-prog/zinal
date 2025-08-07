Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'zinal-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    avatar = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
...             return redirect('/dashboard')
...         return 'Credenciais inválidas.'
...     return render_template('login.html')
... 
... @app.route('/register', methods=['GET', 'POST'])
... def register():
...     if request.method == 'POST':
...         email = request.form['email']
...         password = generate_password_hash(request.form['password'], method='sha256')
...         avatar = request.files['avatar']
...         avatar_path = os.path.join(app.config['UPLOAD_FOLDER'], avatar.filename)
...         avatar.save(avatar_path)
...         user = User(email=email, password=password, avatar=avatar.filename)
...         db.session.add(user)
...         db.session.commit()
...         return redirect('/login')
...     return render_template('register.html')
... 
... @app.route('/dashboard')
... @login_required
... def dashboard():
...     return render_template('dashboard.html')
... 
... @app.route('/homebroker')
... @login_required
... def homebroker():
...     return render_template('homebroker.html')
... 
... @app.route('/logout')
... @login_required
... def logout():
...     logout_user()
...     return redirect('/')
... 
... if __name__ == '__main__':
...     with app.app_context():
...         db.create_all()
...     app.run(debug=True)
