from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from flask_session import Session
from wtforms import StringField, EmailField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, Length
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {
    'sessions': 'sqlite:///sessions.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_SQLALCHEMY_BINDS'] = 'sessions'   # ← вот ключевая строка
app.config['SESSION_KEY_PREFIX'] = 'session:'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SECRET_KEY'] = 'secret'

csrf = CSRFProtect(app)
Session(app)


class User(db.Model): # создание таблицы
    id = db.Column(db.Integer, primary_key=True) # создание полей
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable = False, unique=True)
    password_hash = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def check_login():
    is_user=session.get('user-id')
    if is_user:
        return True
    else:
        return False


class RegisterForm(FlaskForm):
    username = StringField('Name',
                          validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                      validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Enter')


@app.route('/')
def main():
    if check_login():
        return redirect(url_for('profile'))
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    message = None

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first():
            message = "Username is already exist"
            return render_template('register.html', form=form, message=message)
        if User.query.filter_by(email=email).first():
            message = "Email is already exist"
            return render_template('register.html', form=form, message=message)

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        session.clear()
        session['user-id'] = user.id
        session['username'] = user.username
        session['email'] = user.email
        session.permanent = True

        return redirect(url_for('profile'))

    return render_template('register.html', form=form, message=message)


@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    message = None

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session.clear()
            session['user-id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            session.permanent = True
            return redirect(url_for('profile'))
        message = "Invalid username or password"

    return render_template('login.html', form=form, message=message)


@app.route('/profile')
def profile():
    if not check_login():
        return redirect(url_for('index'))
    return render_template('profile.html', username=session.get('username'), email=session.get('email'))


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)