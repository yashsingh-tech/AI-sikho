# app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

from models import db, User
from content import CONTENT

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-this')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ai_sikho.db'

# --- NEW: makes the login cookie survive browser close, for 30 days ---
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)

db.init_app(app)

with app.app_context():
    db.create_all()

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[]
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------- AUTH ROUTES ----------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # --- NEW: password strength check ---
        if len(password) < 8:
            flash('Password must be at least 8 characters long.')
            return redirect(url_for('signup'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('An account with this email already exists.')
            return redirect(url_for('signup'))

        new_user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember=True)
        return redirect(url_for('profile'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            flash('Wrong email or password.')
            return redirect(url_for('login'))

        # --- NEW: remember=True here too ---
        login_user(user, remember=True)

        if user.stream:
            return redirect(url_for('dashboard'))
        return redirect(url_for('profile'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# ---------- PROFILE / ACCOUNT PAGE ----------

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        stream = request.form.get('stream')
        current_user.stream = stream
        db.session.commit()
        return redirect(url_for('dashboard'))

    streams = [{"id": key, "name": val["display_name"]} for key, val in CONTENT.items()]
    return render_template('profile.html', streams=streams)


# --- NEW: separate account page to view/change stream anytime ---
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        stream = request.form.get('stream')
        current_user.stream = stream
        db.session.commit()
        flash('Your learning path has been updated.')
        return redirect(url_for('account'))

    streams = [{"id": key, "name": val["display_name"]} for key, val in CONTENT.items()]
    return render_template('account.html', streams=streams)


# ---------- DASHBOARD ----------

@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.stream:
        return redirect(url_for('profile'))

    stream_data = CONTENT.get(current_user.stream)
    return render_template('dashboard.html', stream_data=stream_data)


# ---------- LESSON DETAIL ----------

@app.route('/lesson/<box_id>/<lesson_id>')
@login_required
def lesson(box_id, lesson_id):
    stream_data = CONTENT.get(current_user.stream)

    box = next((b for b in stream_data['boxes'] if b['id'] == box_id), None)
    lesson_data = next((l for l in box['lessons'] if l['id'] == lesson_id), None)

    return render_template('lesson.html', lesson=lesson_data, box=box)


# ---------- HOME ----------

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')