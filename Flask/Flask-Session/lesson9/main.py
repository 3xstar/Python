from flask import Flask, render_template, redirect, url_for, session, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.secret_key = "32dsfd32423dsfvcs"
app.permanent_session_lifetime = timedelta(minutes=1)

users = {
    1:{"username": "admin", "email": "admin@admin.admin", "age":18}
}

def check_login():
    is_user=session.get('user-id')
    if is_user:
        return True
    else:
        return False

class UserForm(FlaskForm):
    username = StringField('Name',
                          validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email',
                      validators=[DataRequired(), Email()])
    age = IntegerField('Age',
                      validators=[NumberRange(min=1, max=120)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = EmailField('Email',
                      validators=[DataRequired(), Email()])
    submit = SubmitField('Enter')

@app.route('/')
def main():
    is_user = check_login()
    if is_user:
        return f"<h1>You welcome! {session.get('username')}</h1>"
    else:
        return redirect("/login")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    message = None

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        age = form.age.data
        id = max(list(users.keys()))

        session['user-id'] = id
        session['username'] = username
        session['email'] = email
        session['age'] = age
        session.permanent = True

        user = {"username": username, "email": email, "age": age}
        users[id] = user

        return redirect("/")

    return render_template('signup.html', form=form, message=message)


@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    message = None

    if form.validate_on_submit():
        email = form.email.data

        for user in users:
            if users[user]["email"] == email:
                session['user-id'] = user
                session['username'] = users[user]['username']
                session['email'] = email
                session['age'] = users[user]['age']
                session.permanent = True
                return redirect("/")

    return render_template('signin.html', form=form, message=message)

@app.route('/logout')
def logout():
    session.pop('user-id', None)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)